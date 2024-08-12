# Description: This file contains the query builder functions for the storage module.
def buildGetAllQuery(definition):
    entityName = definition["entityName"]
    attributes = [attr["attributeName"] for attr in definition["attributes"]]
    query = f"SELECT {', '.join(attributes)} FROM {entityName}"
    return query