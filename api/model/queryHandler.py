from storage.dbHandler import executeQuery, executeInsert, executeTruncate
from storage.queryBuilder import buildGetAllQuery, buildInsertQuery, buildTruncateQuery
from storage.queryResultParser import parse
from model.behaviorParser import parseBehaviors

def getAll(definition):            
    query = buildGetAllQuery(definition)        
    return executeQuery(lambda rows: parse(rows, definition), query)

def insert(definition, entity_data):
    enhanced_entity_data = parseBehaviors(definition, entity_data)
    query = buildInsertQuery(definition, enhanced_entity_data)
    return executeInsert(query)

def reset(definition):
    query = buildTruncateQuery(definition)
    return executeTruncate(query)