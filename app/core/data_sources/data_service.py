from abc import ABC, abstractmethod
from typing import Any

from pydantic.main import BaseModel

from app.core.serializer_methods.serialize_factory import SerializerFactory
from app.core.lab.laboratory import LabDataItem
from app.core.serializer_methods.serializer import IBaseSerializer, DataFormat
from app.exceptions.lab_exceptions import SerializationError
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class IDataLabService(ABC):
    """Abstract base class for data lab services.

    This abstract class defines the common interface for data lab services. Subclasses should implement the
    `read_data` method to read and process data.

    Attributes:
        _data (Any): The processed data.
        _serializer (IBaseSerializer): The serializer to use for parsing data.
        _lab_object (BaseModel): The Pydantic model representing the lab object.

    Methods:
        read_data: Abstract method to read and process data.
        _process_data_format: Internal method to process data using the serializer.
        get_data: Property to access the processed data.

    """

    _data: Any = None
    _serializer: IBaseSerializer = ...
    _lab_target_class: LabDataItem = ...

    def __init__(self, *, data_format: DataFormat, target_class):
        self._lab_target_class = target_class
        self._serializer = SerializerFactory.create_parser(data_format)

    @abstractmethod
    def _read_data(self, *args, **kwargs) -> Any:
        """Read and process data from a data source.

        Subclasses must implement this method to read data from a specific data source and process it.

        Returns:
            Any: The processed data.
        """
        pass

    def _process_data_format(self):
        """Process data using the specified serializer.

        This method uses the serializer to parse and process raw data.

        Args:
            raw_data: The raw data to be processed.

        Raises:
            SerializationError: If there is an error during serialization.
        """
        try:
            self._data = self._serializer.parse(data=self._data, target_class=self._lab_target_class)
            logger.info(f"Data serialized successfully to target class {self._lab_target_class.__str__()}")
        except SerializationError as e:
            logger.error(e)

    @property
    def get_data(self):
        """Property to access the processed data.

        Returns:
            Any: The processed data.
        """
        return self._data

    def parse_data(self):
        # read the data
        self._read_data()
        # process the data
        self._process_data_format()
