from enum import Enum


class DynamoIndexes(Enum):
    LOCALSECONDARYINDEX = 'lsi'
    GLOBALSECONDARYINDEX = 'gsi'
