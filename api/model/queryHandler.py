from storage.dbHandler import executeQuery
from storage.queryBuilder import buildGetAllQuery
from storage.queryResultParser import parse

def getAll(definition):            
    query = buildGetAllQuery(definition)        
    return executeQuery(lambda rows: parse(rows, definition), query)                    