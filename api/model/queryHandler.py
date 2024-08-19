from storage.dbHandler import executeQuery, executeInsert, executeTruncate
from storage.queryBuilder import buildGetAllQuery, buildInsertQuery, buildTruncateQuery
from storage.queryResultParser import parse

def getAll(definition):            
    query = buildGetAllQuery(definition)        
    return executeQuery(lambda rows: parse(rows, definition), query)

def insert(definition, entity_data):
    query = buildInsertQuery(definition, entity_data)
    return executeInsert(query)

def reset(definition):
    query = buildTruncateQuery(definition)
    return executeTruncate(query)