import unittest
from unittest.mock import patch, MagicMock
from api.storage.sql_handler import SQLHandler

class TestSQLHandler(unittest.TestCase):

    def setUp(self):
        self.sql_handler = SQLHandler()

    @patch('api.storage.sql_handler.SQLHandler.connect')
    @patch('api.storage.sql_handler.SQLHandler.close')
    @patch('api.storage.sql_handler.SQLHandler.cursor', new_callable=MagicMock)
    @patch('api.storage.sql_handler.SQLHandler.connection', new_callable=MagicMock)
    def test_execute_insert_success(self, mock_connection, mock_cursor, mock_close, mock_connect):
        """
        Test that execute_insert successfully executes an insert statement.
        """
        mock_cursor.execute.return_value = None
        mock_connection.commit.return_value = None

        result = self.sql_handler.execute_insert("INSERT INTO test_table (id, name) VALUES (1, 'Alice')")
        self.assertEqual(result, {"Message": "Insert successful"})
        mock_cursor.execute.assert_called_once_with("INSERT INTO test_table (id, name) VALUES (1, 'Alice')")
        mock_connection.commit.assert_called_once()

    @patch('api.storage.sql_handler.SQLHandler.connect')
    @patch('api.storage.sql_handler.SQLHandler.close')
    @patch('api.storage.sql_handler.SQLHandler.cursor', new_callable=MagicMock)
    @patch('api.storage.sql_handler.SQLHandler.connection', new_callable=MagicMock)
    def test_execute_insert_failure(self, mock_connection, mock_cursor, mock_close, mock_connect):
        """
        Test that execute_insert handles exceptions and returns an error message.
        """
        mock_cursor.execute.side_effect = Exception("Insert error")

        result = self.sql_handler.execute_insert("INSERT INTO test_table (id, name) VALUES (1, 'Alice')")
        self.assertEqual(result, {"Message": "Insert failed"})
        mock_cursor.execute.assert_called_once_with("INSERT INTO test_table (id, name) VALUES (1, 'Alice')")
        mock_connection.commit.assert_not_called()

    @patch('api.storage.sql_handler.SQLHandler.connect')
    @patch('api.storage.sql_handler.SQLHandler.close')
    @patch('api.storage.sql_handler.SQLHandler.cursor', new_callable=MagicMock)
    @patch('api.storage.sql_handler.SQLHandler.connection', new_callable=MagicMock)
    def test_execute_truncate_success(self, mock_connection, mock_cursor, mock_close, mock_connect):
        """
        Test that execute_truncate successfully executes a truncate statement.
        """
        mock_cursor.execute.return_value = None
        mock_connection.commit.return_value = None

        result = self.sql_handler.execute_truncate("TRUNCATE TABLE test_table")
        self.assertEqual(result, {"Message": "Truncate successful"})
        mock_cursor.execute.assert_called_once_with("TRUNCATE TABLE test_table")
        mock_connection.commit.assert_called_once()

    @patch('api.storage.sql_handler.SQLHandler.connect')
    @patch('api.storage.sql_handler.SQLHandler.close')
    @patch('api.storage.sql_handler.SQLHandler.cursor', new_callable=MagicMock)
    @patch('api.storage.sql_handler.SQLHandler.connection', new_callable=MagicMock)
    def test_execute_truncate_failure(self, mock_connection, mock_cursor, mock_close, mock_connect):
        """
        Test that execute_truncate handles exceptions and returns an error message.
        """
        mock_cursor.execute.side_effect = Exception("Truncate error")

        result = self.sql_handler.execute_truncate("TRUNCATE TABLE test_table")
        self.assertEqual(result, {"Message": "Truncate failed"})
        mock_cursor.execute.assert_called_once_with("TRUNCATE TABLE test_table")
        mock_connection.commit.assert_not_called()

if __name__ == '__main__':
    unittest.main()