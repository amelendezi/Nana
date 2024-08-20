from abc import ABC, abstractmethod

class AttributeValidation(ABC):
    @abstractmethod
    def validate(self, attribute_name, value):
        pass