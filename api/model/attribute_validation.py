from abc import ABC, abstractmethod

class AttributeValidation(ABC):
    @abstractmethod
    def validate(self, attribute_name, value):
        pass

class RequiredValidation(AttributeValidation):
    def validate(self, attribute_name, value):
        if value is None or value == "":
            return f"{attribute_name} is required."
        return None

class MaxLengthValidation(AttributeValidation):
    def __init__(self, max_length):
        self.max_length = max_length

    def validate(self, attribute_name, value):
        if value is None:
            return None
        if len(value) > self.max_length:
            return f"{attribute_name} exceeds maximum length of {self.max_length}."
        return None