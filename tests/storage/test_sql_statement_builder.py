import unittest
from api.storage.sql_statement_builder import SQLStatementBuilder

class TestSQLStatementBuilder(unittest.TestCase):

    def setUp(self):
        self.builder = SQLStatementBuilder()
        self.definition = {
            "entityName": "test_entity",
            "attributes": [
                {"attributeName": "id"},
                {"attributeName": "name"},
                {"attributeName": "age"}
            ]
        }
        self.entity_data = {
            "id": 1,
            "name": "Alice",
            "age": 30
        }

    def test_build_get_all_query(self):
        """
        Test that build_get_all_query correctly builds a SELECT query.
        """
        expected_query = "SELECT id, name, age FROM test_entity"
        query = self.builder.build_get_all_query(self.definition)
        self.assertEqual(query, expected_query)

    def test_build_insert_query(self):
        """
        Test that build_insert_query correctly builds an INSERT query.
        """
        expected_query = "INSERT INTO test_entity (id, name, age) VALUES ('1', 'Alice', '30')"
        query = self.builder.build_insert_query(self.definition, self.entity_data)
        self.assertEqual(query, expected_query)

    def test_build_insert_query_empty_attributes(self):
        """
        Test that build_insert_query raises a ValueError when attributes or values are empty.
        """
        with self.assertRaises(ValueError):
            self.builder.build_insert_query(self.definition, {})

    def test_build_truncate_query(self):
        """
        Test that build_truncate_query correctly builds a TRUNCATE TABLE query.
        """
        expected_query = "TRUNCATE TABLE test_entity"
        query = self.builder.build_truncate_query(self.definition)
        self.assertEqual(query, expected_query)

if __name__ == '__main__':
    unittest.main()