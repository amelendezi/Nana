from model.validations.attribute_validation import AttributeValidation

class MaxLengthValidation(AttributeValidation):
    def __init__(self, max_length):
        self.max_length = max_length

    def validate(self, attribute_name, value):
        if value is None:
            return None
        if len(value) > self.max_length:
            return f"{attribute_name} exceeds maximum length of {self.max_length}."
        return None