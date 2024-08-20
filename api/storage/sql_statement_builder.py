# Description: This file contains the query builder functions for the storage module.
class SQLStatementBuilder:
    
    def __init__(self) -> None:
        pass
    
    def build_get_all_query(self, definition):
        entity_name = definition["entityName"]
        attributes = [attr["attributeName"] for attr in definition["attributes"]]
        query = f"SELECT {', '.join(attributes)} FROM {entity_name}"
        return query

    def build_insert_query(self, definition, entity_data):
        entity_name = definition["entityName"]
        attributes = [attr["attributeName"] for attr in definition["attributes"] if attr["attributeName"] in entity_data]
        values = [f"'{entity_data[attr]}'" for attr in attributes]
        
        if not attributes or not values:
            raise ValueError("Attributes or values cannot be empty")

        query = f"INSERT INTO {entity_name} ({', '.join(attributes)}) VALUES ({', '.join(values)})"
        return query
    
    def build_truncate_query(self, definition):
        entity_name = definition["entityName"]
        query = f"TRUNCATE TABLE {entity_name}"
        return query