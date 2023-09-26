from pathlib import Path
from typing import Any

from fastapi import UploadFile

from app.core.data_sources.data_service import IDataLabService
from app.core.lab.laboratory import LabDataItem
from app.core.serializer_methods.serializer import IBaseSerializer
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class FileSource(IDataLabService):
    """Represents a data source for reading data from an uploaded file.

    This class is designed to read data from an uploaded file and process it using a specified serializer.

    Attributes:
        file (UploadFile): The uploaded file to read data from.
        _serializer (IBaseSerializer): The serializer to use for parsing data.

    Methods:
        read_data: Read and process data from the uploaded file.

    """

    def __init__(self, file: UploadFile, serializer: IBaseSerializer, lab_class: LabDataItem):
        super().__init__(serializer=serializer, target_class=lab_class)
        self.file = file
        self._serializer = serializer

    def read_data(self, *args, **kwargs) -> Any:
        """Read and process data from the uploaded file.

        This method reads data from the uploaded file, processes it using the specified serializer,
        and returns the processed data.

        Returns:
            Any: The processed data.
        """
        # Read the data from the file into a string
        self._data = self.file.read()


class ReadFileSource(IDataLabService):
    """Represents a data source for future reading from a file path.

    This class is designed for scenarios where data will be read from a file path in the future.
    It serves as a placeholder for such operations. Important to understand it!

    Attributes:
        file (Path): The file path to read data from.
        _serializer (IBaseSerializer): The serializer to use for parsing data.

    Methods:
        read_data: This method is not implemented and raises a NotImplementedError.

    """

    def __init__(self, *,
                 file_path: Path,
                 serializer: IBaseSerializer,
                 lab_class: LabDataItem, target_class):
        super().__init__(serializer=serializer, target_class=target_class)
        self.file_path = file_path

    def read_data(self, *args, **kwargs) -> Any:
        """Read and process data from the file path.

        This method is not implemented and raises a NotImplementedError.

        Raises:
            NotImplementedError: This method is not implemented in this class.
        """
        raise NotImplementedError()
