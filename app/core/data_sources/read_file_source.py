from app.core.data_sources.data_service import IDataLabService
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


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
        logger.info("yay")

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
