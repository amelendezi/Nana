# Description: this parses the result from a query using the definition to a result array.
class SQLResultParser:
    
    def __init__(self) -> None:
        pass
        
    def map_rows_to_definition_result(self, rows, definition):
        attributes = [attr["attributeName"] for attr in definition["attributes"]]
        result = []
        for row in rows:
            entity = {attributes[i]: row[i] for i in range(len(attributes))}
            result.append(entity)
        return result