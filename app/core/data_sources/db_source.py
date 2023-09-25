from abc import abstractmethod

from elasticsearch import Elasticsearch

from app.core.data_sources.data_source import IDataLabService


class DbSource(IDataLabService):
    def __init__(self, host, port, *args, **kwargs):
        self.host = host
        self.port = port

    @abstractmethod
    def read_data(self, *args, **kwargs):
        raise NotImplementedError("Non implemented yet!")


class ElasticSource(DbSource):
    def __init__(self, index_name, host, port=9200, *args, **kwargs):
        super().__init__(host, port, *args, **kwargs)
        self.index_name = index_name
        self.es = Elasticsearch([{'host': self.host, 'port': self.port}])

    def read_data(self, *args, **kwargs):
        raise NotImplementedError("Non implemented yet!")


