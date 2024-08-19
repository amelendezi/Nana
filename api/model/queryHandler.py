from storage.dbHandler import executeQuery, executeInsert
from storage.queryBuilder import buildGetAllQuery, buildInsertQuery
from storage.queryResultParser import parse

def getAll(definition):            
    query = buildGetAllQuery(definition)        
    return executeQuery(lambda rows: parse(rows, definition), query)

def insert(definition, entity_data):
    query = buildInsertQuery(definition, entity_data)
    return executeInsert(query)