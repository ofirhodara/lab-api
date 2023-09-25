from abc import ABC, abstractmethod
from typing import Any

from app.core.serializer_methods.serializer import IBaseSerializer
from app.exceptions.lab_exceptions import SerializationError
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class IDataLabService(ABC):
    _data: Any
    _serializer: IBaseSerializer
    _lab_object:

    @abstractmethod
    def read_data(self, *args, **kwargs) -> Any:
        pass

    def _process_data_format(self, raw_data):
        try:
            self._data = self._serializer.parse(raw_data)
        except SerializationError as e:
            logger.error(e)

    @property
    def get_data(self):
        return self._data
