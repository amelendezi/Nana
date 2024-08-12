import json
import os

class DefinitionNotFoundException(Exception):
	def __init__(self, entity):
		super().__init__(f"Definition for entity '{entity}' not found.")

def getDefinition(entity):
	# Construct the definition file path
	definition_file_path = os.path.join('api', 'model', 'definitions', f'{entity}_definition.json')
	
	# Check if the file exists
	if os.path.exists(definition_file_path):
		# Load and return the definition
		with open(definition_file_path, 'r') as definition_file:
			definition = json.load(definition_file)
		return definition
	else:
		# Throw an exception if the file does not exist
		raise DefinitionNotFoundException(entity)