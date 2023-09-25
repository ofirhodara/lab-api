from app.core.data_sources.data_source import DataSource


class DbSource(DataSource):
    def __init__(self, host, port, table, sql_query):
        self.host = host
        self.port = port
        self.table = table
        self.sql_query = sql_query

    def read_data(self, *args, **kwargs):
        pass

# TODO: Redis, Elastic.....
