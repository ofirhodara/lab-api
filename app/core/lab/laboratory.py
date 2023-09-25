from typing import List, Dict, Generic

from pydantic import BaseModel
from result import Ok, Err

from app.core.lab.items import Port, Card, Component
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class LabDataItem(BaseModel):
    pass


class Laboratory(LabDataItem):
    """Represents a laboratory with components, cards, and ports.

    This Pydantic model represents a laboratory with its various components, cards, and ports.

    Attributes:
        _laboratory_class_mapper (Dict[str, BaseModel]): A mapping of class names to their corresponding Pydantic models.
        component (List[Component]): A list of Component instances.
        cards (List[Card]): A list of Card instances.
        ports (List[Port]): A list of Port instances.

    Methods:
        get_lab_class_by_name: Retrieve a class type based on its name.

    """

    _laboratory_class_mapper: Dict[str, BaseModel] = {
        "Component": Component,
        "Card": Card,
        "Port": Port
    }
    component: List[Component]
    cards: List[Card]
    ports: List[Port]

    @staticmethod
    def get_lab_class_by_name(class_name: str) -> Generic:
        """Retrieve a class type based on its name.

        This static method allows you to retrieve a class type (Pydantic model) based on its name.
        It is useful for dynamically selecting a model based on input data.

        Args:
            class_name (str): The name of the class to retrieve.

        Returns:
            Generic: An instance of the class if found, or an error result if not found.

        """
        if class_name in Laboratory._laboratory_class_mapper.keys():
            return Ok(Laboratory._laboratory_class_mapper[class_name])
        e_message = f"The class {class_name} is not one of our Laboratory items classes"
        logger.fatal(e_message)
        return Err(e_message)
