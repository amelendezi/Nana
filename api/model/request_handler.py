from storage.sql_handler import SQLHandler
from storage.sql_statement_builder import SQLStatementBuilder
from storage.sql_result_parser import SQLResultParser
from model.behavior_handler import BehaviorHandler

class RequestHandler:
    
    def __init__(self) -> None:
        self.db_handler = SQLHandler()
        self.statement_builder = SQLStatementBuilder()
        self.behavior_handler = BehaviorHandler()
        self.sql_result_parser = SQLResultParser()
        
    def get_all(self, definition):            
        query = self.statement_builder.build_get_all_query(definition)
        return self.db_handler.execute_query(lambda rows: self.sql_result_parser.map_rows_to_definition_result(rows, definition), query)

    def insert(self, definition, entity_data):    
        enhanced_entity_data = self.behavior_handler.handle(definition, entity_data)
        query = self.statement_builder.build_insert_query(definition, enhanced_entity_data)
        return self.db_handler.execute_insert(query)

    def reset(self, definition):
        query = self.statement_builder.build_truncate_query(definition)
        return self.db_handler.execute_truncate(query)