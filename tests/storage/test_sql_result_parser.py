import unittest
from api.storage.sql_result_parser import SQLResultParser

class TestSQLResultParser(unittest.TestCase):

    def setUp(self):
        self.parser = SQLResultParser()
        self.definition = {
            "attributes": [
                {"attributeName": "id"},
                {"attributeName": "name"},
                {"attributeName": "age"}
            ]
        }
        self.rows = [
            (1, "Alice", 30),
            (2, "Bob", 25)
        ]

    def test_map_rows_to_definition_result(self):
        """
        Test that map_rows_to_definition_result correctly maps rows to the definition result.
        """
        expected_result = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25}
        ]
        result = self.parser.map_rows_to_definition_result(self.rows, self.definition)
        self.assertEqual(result, expected_result)

    def test_map_rows_to_definition_result_empty_rows(self):
        """
        Test that map_rows_to_definition_result returns an empty list when rows are empty.
        """
        result = self.parser.map_rows_to_definition_result([], self.definition)
        self.assertEqual(result, [])

    def test_map_rows_to_definition_result_empty_definition(self):
        """
        Test that map_rows_to_definition_result returns an empty list when definition is empty.
        """
        empty_definition = {"attributes": []}
        result = self.parser.map_rows_to_definition_result(self.rows, empty_definition)
        self.assertEqual(result, [{} for _ in self.rows])

if __name__ == '__main__':
    unittest.main()