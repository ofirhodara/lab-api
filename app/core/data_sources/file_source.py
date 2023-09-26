from abc import ABC
from pathlib import Path
from typing import Any

from fastapi import UploadFile

from app.core.data_sources.data_service import IDataLabService
from app.core.lab.laboratory import LabDataItem
from app.core.serializer_methods.data_formats import DataFormat
from app.core.serializer_methods.serializer import IBaseSerializer
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class FileSource(IDataLabService):
    """Represents a data source for reading data from an uploaded file.

    This class is designed to read data from an uploaded file and process it using a specified serializer.

    Attributes:
        file (UploadFile): The uploaded file to read data from.


    Methods:
        read_data: Read and process data from the uploaded file.

    """

    def __init__(self, file: UploadFile, data_format: DataFormat, lab_class: LabDataItem):
        super().__init__(target_class=lab_class, data_format=data_format)
        self.file = file

    def _read_data(self, *args, **kwargs) -> Any:
        """Read and process data from the uploaded file.

        This method reads data from the uploaded file, processes it using the specified serializer,
        and returns the processed data.

        Returns:
            Any: The processed data.
        """

        try:
            # Read the data from the file into a string
            self._data = self.file.read()

        except IOError as e:
            err_msg = f"IO Error while trying to open file from path {str(self.file)}"
            logger.fatal(err_msg)
            raise FileNotFoundError(err_msg)
        except Exception as e:
            err_msg = f"An error occurred: {e}"
            logger.fatal(err_msg)
            raise e


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
                 data_format: DataFormat,
                 lab_class: LabDataItem):
        """

        Returns:
            object:
        """
        super().__init__(target_class=lab_class, data_format=data_format)
        self.file_path = file_path

    def _read_data(self) -> Any:
        """Read and process data from the file path.

        This method is not implemented and raises a NotImplementedError.

        Raises:
            NotImplementedError: This method is not implemented in this class.
        """
        try:
            with open(self.file_path, "r") as file:
                self._data = file.read()
        except FileNotFoundError as e:
            err_msg = f"The file {self.file_path} does not exist."
            logger.fatal(err_msg)
            raise FileNotFoundError(err_msg)
        except IOError as e:
            err_msg = f"IO Error while trying to open file from path {self.file_path}"
            logger.fatal(err_msg)
            raise FileNotFoundError(err_msg)
        except Exception as e:
            err_msg = f"An error occurred: {e}"
            logger.fatal(err_msg)
            raise e
