import unittest
import os
import json
from api.model.definitions_provider import DefinitionsProvider, DefinitionNotFoundException

class TestDefinitionsProvider(unittest.TestCase):

    def setUp(self):
        self.provider = DefinitionsProvider()
        self.test_entity = 'test_entity'
        self.test_definition_path = os.path.join('api', 'model', 'definitions', f'{self.test_entity}_definition.json')
        
        # Create a sample definition file for testing
        self.sample_definition = {"key": "value"}
        os.makedirs(os.path.dirname(self.test_definition_path), exist_ok=True)
        with open(self.test_definition_path, 'w') as f:
            json.dump(self.sample_definition, f)

    def tearDown(self):
        # Remove the sample definition file after tests
        if os.path.exists(self.test_definition_path):
            os.remove(self.test_definition_path)

    def test_get_definition_success(self):
        """
        Test that getDefinition successfully retrieves the definition
        for an existing entity.
        """
        definition = self.provider.getDefinition(self.test_entity)
        self.assertEqual(definition, self.sample_definition)

    def test_get_definition_not_found(self):
        """
        Test that getDefinition raises a DefinitionNotFoundException
        when the definition for a non-existent entity is requested.
        """
        with self.assertRaises(DefinitionNotFoundException):
            self.provider.getDefinition('non_existent_entity')

if __name__ == '__main__':
    unittest.main()