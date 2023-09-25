from pathlib import Path
from typing import Any

from fastapi import UploadFile

from app.core.data_sources.data_source import IDataLabService
from app.core.serializer_methods.serializer import IBaseSerializer
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class FileSource(IDataLabService):
    def __init__(self, file: UploadFile, _serializer: IBaseSerializer):
        self.file = file
        self._serializer = _serializer

    def read_data(self, *args, **kwargs) -> Any:
        # handle the data into string from files
        raw_data = self.file.read()
        super()._process_data_format(self.file)


class ReadFileSource(IDataLabService):
    """
    Consider we want the server to read the data from file path
    i will send him as request the file path to read from and it will do it for me
    so we have one classic FileSource and the second one will be for future reading
    """

    def __init__(self, file_path: Path, _serializer: IBaseSerializer):
        self.file = file_path
        self._serializer = _serializer

    def read_data(self, *args, **kwargs) -> Any:
        raise NotImplementedError()
