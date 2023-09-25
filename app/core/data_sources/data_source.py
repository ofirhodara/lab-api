from abc import ABC, abstractmethod
from typing import Any




class DataSource(ABC):
    _data: Any
    _serializer: BaseSerializer
    @abstractmethod
    def read_data(self, *args, **kwargs) -> Any:
        pass

    @property
    def get_data(self):
        return self._data
