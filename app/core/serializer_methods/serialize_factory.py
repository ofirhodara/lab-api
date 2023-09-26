from typing import Dict

from result import Ok, Err

from app.core.serializer_methods.data_formats import DataFormat
from app.core.serializer_methods.models_serializeres import CsvSerializer, YamlSerializer
from app.core.serializer_methods.serializer import IBaseSerializer
from app.exceptions.lab_exceptions import SerializerFactoryError
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class SerializerFactory:
    """Factory class for creating parsers."""

    _mapper: Dict[str, IBaseSerializer] = {
        DataFormat.YAML.value: YamlSerializer,
        DataFormat.CSV.value: CsvSerializer
    }

    @staticmethod
    def create_parser(data_format: DataFormat) -> IBaseSerializer:
        """Create a parser based on the data format.

        Args:
            data_format (DataFormat): The data format to determine the parser for.

        Returns:
            Ok: An Ok result containing the parser if the format is supported.
            Err: An Err result with an error message if the format is unsupported.
        """

        if data_format.value in SerializerFactory._mapper.keys():
            factory_instance: IBaseSerializer = SerializerFactory._mapper[data_format.value]()
            return factory_instance

        e_message = f"Error Unsupported data format {data_format.value}"
        logger.error(e_message)
        raise SerializerFactoryError(e_message)
