class SerializationError(Exception):
    def __init__(self, message="Error during serialization"):
        self.message = message
        super().__init__(self.message)


class SerializerFactoryError(Exception):
    def __init__(self, message="Error during trying to build serializer"):
        self.message = message
        super().__init__(self.message)
