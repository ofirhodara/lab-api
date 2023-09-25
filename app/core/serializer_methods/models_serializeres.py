import csv

import yaml

from app.core.serializer_methods.serializer import IBaseSerializer


class YamlSerializer(IBaseSerializer):
    def parse(self, data, target_class):
        parsed_data = yaml.safe_load(data)
        instance = target_class()
        for key, value in parsed_data.items():
            setattr(instance, key, value)
        return instance


class CsvSerializer(IBaseSerializer):
    def parse(self, data, target_class):
        rows = csv.DictReader(data.splitlines())  # Assumes data is a CSV string
        instance_list = []

        for row in rows:
            instance = target_class()
            for key, value in row.items():
                setattr(instance, key, value)
            instance_list.append(instance)

        return instance_list
