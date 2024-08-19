# Description: This file contains the query builder functions for the storage module.
def buildGetAllQuery(definition):
    entityName = definition["entityName"]
    attributes = [attr["attributeName"] for attr in definition["attributes"]]
    query = f"SELECT {', '.join(attributes)} FROM {entityName}"
    return query

def buildInsertQuery(definition, entity_data):
    entityName = definition["entityName"]
    attributes = [attr["attributeName"] for attr in definition["attributes"] if attr["attributeName"] in entity_data]
    values = [f"'{entity_data[attr]}'" for attr in attributes]
    
    if not attributes or not values:
        raise ValueError("Attributes or values cannot be empty")

    query = f"INSERT INTO {entityName} ({', '.join(attributes)}) VALUES ({', '.join(values)})"
    return query