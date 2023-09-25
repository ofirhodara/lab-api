from app.core.data_sources.data_source import DataSource


class DbSource(DataSource):
    def __init__(self, host, port, connection_str, *args, **kwargs):
        self.host = host
        self.port = port
        self.connection_str = connection_str

    @abstract_method
    def read_data(self, *args, **kwargs):
        raise NotImplementedError("Non implemented yet!")


class ElasticSource(DbSource):
    def __init__(self, index, host, port, connection_str, *args, **kwargs):
        super().__init__(host, port, connection_str, *args, **kwargs)
        self.index = index

    def read_data(self, *args, **kwargs):
        raise NotImplementedError("Non implemented yet!")

# TODO: Redis, Elastic.....
