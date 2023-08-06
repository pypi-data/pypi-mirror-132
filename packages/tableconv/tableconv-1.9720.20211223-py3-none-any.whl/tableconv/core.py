import logging
import os
import sys
import tempfile
from typing import Any, Dict, List, Tuple

import urllib.parse
import ciso8601
import pandas as pd
from pandas.errors import EmptyDataError

from .adapters.df import read_adapters, write_adapters
from .adapters.df.base import Adapter
from .in_memory_query import query_in_memory
from .uri import parse_uri

logger = logging.getLogger(__name__)


def resolve_query_arg(query: str) -> str:
    if not query:
        return None

    if sys.version_info.major > 3 or (sys.version_info.major == 3 and sys.version_info.minor >= 9):
        query = query.removeprefix('file://')
    else:
        if query.startswith('file://'):
            query = query[len('file://'):]

    potential_snippet_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'snippets', query)
    if os.path.exists(potential_snippet_path):
        with open(potential_snippet_path) as f:
            return f.read().strip()

    if os.path.exists(query):
        with open(query) as f:
            return f.read().strip()

    return query


class SuppliedDataError(RuntimeError):
    pass


class IntermediateExchangeTable:
    def __init__(self, df=None, from_df: pd.DataFrame = None, from_dict_records: List[Dict[str, Any]] = None):
        """
        tableconv's abstract intermediate tabular data type.

        Normally you should acquire a ``IntermediateExchangeTable`` by loading in data from a URL using :ref:load_url.
        However, if your data is already in a python native datatype, you can directly put it into a
        ``IntermediateExchangeTable`` by passing it in using one of the two available Python native forms:

        :param from_df:
            Wrap the provided Pandas Dataframe in a IntermediateExchangeTable.
        :param from_dict_records:
            Wrap the provided List of Dict records in a IntermediateExchangeTable.
        """
        if sum([df is not None, from_df is not None, from_dict_records is not None]) != 1:
            raise ValueError('Please pass one and only one of either df, from_df, or from_dict_records')
        if df is not None:
            self.df = df
        if from_df is not None:
            self.df = from_df
        if from_dict_records is not None:
            self.df = pd.DataFrame.from_dict(from_dict_records, orient='records')

    def dump_to_url(self, url: str, params: Dict[str, Any] = None) -> str:
        """
        Export the table in the format and location identified by url.

        :return:
            A "permalink" url that can be used to access the exported data. This URL is normally identical to the URL
            that was passed in, but not always in cases where e.g. a new ID needed to be dynamically generated during
            the export, or in cases when the passed in URL was relative or otherwise vague.
        """
        scheme = parse_uri(url).scheme
        try:
            write_adapter = write_adapters[scheme]
        except KeyError:
            logger.error(f'Unsupported scheme {scheme}. Please see --help.')
            sys.exit(1)

        if params:
            # TODO: This is a total hack! Implementing real structured table references, including structured passing of
            # params to adapters, is still pending. Right now everything is stringly-typed internally.
            assert '?' not in url
            url += f'?{urllib.parse.urlencode(params)}'
        logger.debug(f'Exporting data out via {write_adapter.__qualname__} to {url}')
        return write_adapter.dump(self.df, url)

    def get_json_schema(self):
        """
        Warning: This is just experimental / exploratory. The current implementation is also buggy.
        """
        # Consider instead using https://github.com/pandas-dev/pandas/blob/v1.3.2/pandas/io/json/_table_schema.py
        from genson import SchemaBuilder
        builder = SchemaBuilder()
        builder.add_schema({'type': 'object', 'properties': {}})
        for row in self.df.to_dict(orient='records'):
            builder.add_object(row)
        return builder.to_schema()

    def transform_in_memory(self, sql):
        # TODO refactor to use this
        pass

    def as_dict_records(self) -> List[Dict[str, Any]]:
        """
        Expose the loaded data as a List of Dict records.
        """
        return self.as_pandas_df.to_dict(orient='records')

    def as_pandas_df(self) -> pd.DataFrame:
        """
        Expose the loaded data as a Pandas Dataframe.

        Warning: Mutating the provided DataFrame may corrupt the internal state of the ``IntermediateExchangeTable``
        and prevent the ``IntermediateExchangeTable`` from being used further. If you want to expose as a DataFrame,
        mutate it, and then also continue to use the same ``IntermediateExchangeTable`` afterwards, then please take a
        copy (copy.deepcopy) of the exposed DataFrame.
        """
        return self.df


FSSPEC_SCHEMES = {'https', 'http', 'ftp', 's3', 'gcs', 'sftp', 'scp', 'abfs'}


def parse_source_url(url: str) -> Tuple[str, Adapter]:
    """ Returns source_scheme, read_adapter """
    parsed_url = parse_uri(url)
    source_scheme = parsed_url.scheme

    if source_scheme in FSSPEC_SCHEMES:
        source_scheme = os.path.splitext(parsed_url.path)[1][1:]

    if source_scheme is None:
        logger.error(f'Unable to parse URL "{url}". Please see --help.')
        sys.exit(1)

    try:
        read_adapter = read_adapters[source_scheme]
    except KeyError:
        logger.error(f'Unsupported scheme {source_scheme}. Please see --help.')
        sys.exit(1)

    return source_scheme, read_adapter


def process_and_rewrite_remote_source_url(url: str) -> str:
    """
    If source is a remote file, download a local copy of it first and then rewrite the URL to reference the downloaded
    file.

    Note: This is an experimental undocumented feature that probably will not continue to be supported in the future.
    Note: This implementation is pretty hacky.
    """
    import fsspec
    logger.info('Source URL is a remote file - attempting to create local copy (via fsspec)')
    temp_file = tempfile.NamedTemporaryFile()
    parsed_url = parse_uri(url)
    with fsspec.open(f'{parsed_url.scheme}://{parsed_url.authority}{parsed_url.path}') as network_file:
        temp_file.write(network_file.read())
    temp_file.flush()
    encoded_query_params = '?' + '&'.join((f'{key}={value}' for key, value in parsed_url.query.items()))
    new_url = f'{os.path.splitext(parsed_url.path)[1][1:]}://{temp_file.name}{encoded_query_params if parsed_url.query else ""}'
    logger.info(f'Cached remote file as {new_url}')
    return new_url


def validate_coercion_schema(schema):
    SCHEMA_COERCION_SUPPORTED_TYPES = {'datetime', 'str', 'int', 'float'}
    unsupported_schema_types = set(schema.values()) - SCHEMA_COERCION_SUPPORTED_TYPES
    if unsupported_schema_types:
        raise ValueError(f'Unsupported schema type(s): {", ".join(unsupported_schema_types)}')


def coerce_schema(df, schema, restrict_schema):
    validate_coercion_schema(schema)

    # Add missing columns
    for col in set(schema.keys()) - set(df.columns):
        df[col] = None

    # Coerce the type of pre-existing columns
    for col in set(schema.keys()).intersection(set(df.columns)):
        if schema[col] == 'datetime':
            df[col] = df.apply(
                lambda r: ciso8601.parse_datetime(r[col]) if r[col] not in (None, '') else None, axis=1
            )
        elif schema[col] == 'str':
            df[col] = df[col].astype('string')
        elif schema[col] == 'int':
            df[col] = df.apply(
                lambda r: int(r[col]) if r[col] not in (None, '') else None, axis=1
            )
            # df[col] = pd.to_numeric(df[col], downcast='integer')
        elif schema[col] == 'float':
            df[col] = df.apply(
                lambda r: float(r[col]) if r[col] not in (None, '') else None, axis=1
            )

    if restrict_schema:
        # Drop all other columns
        df = df[schema.keys()]

    return df


def load_url(url: str, params: Dict[str, Any] = None, query: str = None, filter_sql: str = None,
             schema_coercion: Dict[str, str] = None, restrict_schema: bool = False) -> IntermediateExchangeTable:
    """
    Load the data referenced by ``url`` into tableconv's abstract intermediate tabular data type
    (:ref:`IntermediateExchangeTable`).

    :param url:
        This can be any URL referencing tabular or psuedo-tabular data. Refer to :ref:Adapters for the supported
        formats.
    :param params:
        These are URL query parameters to add into the URL, for setting various Adapter options. Refer to the
         :ref:Adapters documentation for details.
    :param query:
        To extract only some of the data, provide a query here, to run on the data. This will need to be written in the
        native query language of whatever ddata format you are extracting data from (e.g. SQL for a SQL database), or
        for formats without a native query language (e.g. CSV), the DuckDB SQL syntax is normally supported. Refer to
        the :ref:Adapters documentation for details.
    :param fiter_sql:
        You can transform the data in-memory after loading it by passing in a ``filter_sql`` SELECT query.
        Transformations are powered by DuckDB and uses the DuckDB SQL syntax. Reference the table named ``data`` for
        the raw imported data.
    :param schema_coercion:
        This is an experimental feature. Subject to change. Docummentation unavailable.
    :param restrict_schema:
        This is an experimental feature. Subject to change. Docummentation unavailable.
    """
    if parse_uri(url).scheme in FSSPEC_SCHEMES:
        url = process_and_rewrite_remote_source_url(url)

    source_scheme, read_adapter = parse_source_url(url)
    query = resolve_query_arg(query)  # TODO: Dynamic file resolution is great for CLI but it isn't appropriate for the Python API.
    filter_sql = resolve_query_arg(filter_sql)

    if params:
        # TODO: This is a total hack! Implementing real structured table references, including structured passing of
        # params to adapters, is still pending. Right now everything is stringly-typed internally.
        assert '?' not in url
        url += f'?{urllib.parse.urlencode(params)}'

    logger.debug(f'Loading data in via {read_adapter.__qualname__} from {url}')
    try:
        df = read_adapter.load(url, query)
    except EmptyDataError as e:
        raise SuppliedDataError(f'Empty data source {url}: {str(e)}') from e
    if df.empty:
        raise SuppliedDataError(f'Empty data source {url}')

    # Schema coercion
    if schema_coercion:
        df = coerce_schema(df, schema_coercion, restrict_schema)

    # Run in-memory filters
    if filter_sql:
        logger.debug('Running intermediate filter sql query in-memory')
        df = query_in_memory(df, filter_sql)

    if df.empty:
        raise SuppliedDataError('No rows returned by intermediate filter sql query')

    table = IntermediateExchangeTable(df)
    table.source_scheme = source_scheme

    return table
