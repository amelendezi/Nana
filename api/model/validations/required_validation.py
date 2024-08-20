from model.validations.attribute_validation import AttributeValidation 

class RequiredValidation(AttributeValidation):
    def validate(self, attribute_name, value):
        if value is None or value == "":
            return f"{attribute_name} is required."
        return None