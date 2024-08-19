def validate_required(attribute_name, value):
    if value is None or value == "":
        return f"{attribute_name} is required."
    return None

def validate_max_length(attribute_name, value, max_length):
    if value is None:
        return None
    if len(value) > max_length:
        return f"{attribute_name} exceeds maximum length of {max_length}."
    return None

def validate_form_data(definition, form_data):
    response_messages = []
    
    for attribute in definition["attributes"]:
        attribute_name = attribute["attributeName"]
        validations = attribute.get("validations", [])
        
        value = form_data.get(attribute_name)
        
        for validation in validations:
            
            validationType = validation.get("type")
            
            # Check if the validation is required
            if validationType == "Required":
                message = validate_required(attribute_name, value)
                if message:
                    response_messages.append(message)
                    
            # Check if the validation is MaxLength
            elif validationType == "MaxLength":
                max_length = int(validation.get("value"))                
                message = validate_max_length(attribute_name, value, max_length)
                if message:
                    response_messages.append(message)
    
    return response_messages