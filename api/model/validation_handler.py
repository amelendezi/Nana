from model.attribute_validation import AttributeValidation, RequiredValidation, MaxLengthValidation

class ValidationHandler:
    
    def __init__(self) -> None:    
        pass
    
    def apply_validation(self, validation: AttributeValidation, attribute_name, value):
        return validation.validate(attribute_name, value)

    def validate_form_data(self, definition, form_data):
        response_messages = []
        
        for attribute in definition["attributes"]:
            attribute_name = attribute["attributeName"]
            validations = attribute.get("validations", [])
            
            value = form_data.get(attribute_name)
            
            for validation in validations:
                validation_type = validation.get("type")
                            
                if validation_type == "Required":
                    validator = RequiredValidation()
                elif validation_type == "MaxLength":
                    max_length = int(validation.get("value"))
                    validator = MaxLengthValidation(max_length)
                else:
                    continue
                
                message = self.apply_validation(validator, attribute_name, value)
                if message:
                    response_messages.append(message)
        
        return response_messages