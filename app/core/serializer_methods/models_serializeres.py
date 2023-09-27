"""
Module: serializers.py

This module defines two serializers, YamlSerializer and CsvSerializer, that implement the IBaseSerializer interface.
"""

import csv
from typing import Any

import yaml

from app.core.lab.laboratory import LabDataItem
from app.core.serializer_methods.serializer import IBaseSerializer


class YamlSerializer(IBaseSerializer):
    """
    YamlSerializer class implements the IBaseSerializer interface for parsing YAML data into LabDataItem objects.
    for example the yaml will look like:



    """

    def serialize(self, data: Any, target_class: LabDataItem):
        """
        Parses YAML data and creates an instance of the target class.
        the yaml file will look like this in order to work with my infrastructure
        deserializable_objects:
          port:
          - port_one:
              name: ofir
              age: 4
          - port_two: and so on..

        Args:
            data (Any): YAML data to be parsed.
            target_class (LabDataItem): The class into which the data should be parsed.

        Returns:
            LabDataItem: An instance of the target_class with attributes set from the parsed data.
        """

        ...


class CsvSerializer(IBaseSerializer):
    """
    CsvSerializer class implements the IBaseSerializer interface for parsing CSV data into a list of LabDataItem objects.
    """

    def serialize(self, data, target_class):
        """
        Parses CSV data and creates a list of instances of the target class.

        Args:
            data (str): CSV data (as a string) to be parsed.
            target_class: The class into which each row of data should be parsed.

        Returns:
            list: A list of instances of the target_class, with attributes set from the parsed CSV data.
        """
        rows = csv.DictReader(data.splitlines())  # Assumes data is a CSV string
        instance_list = []

        for row in rows:
            instance = target_class()
            for key, value in row.items():
                setattr(instance, key, value)

            instance_list.append(instance)
        return instance_list
