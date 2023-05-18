def get_parameters(table_name):
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id', 'KeyType': 'HASH'},  # partition_key
            {'AttributeName': 'firstname', 'KeyType': 'RANGE'}  # sort_key
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'id', 'AttributeType': 'N'},
            {'AttributeName': 'firstname', 'AttributeType': 'S'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    }
    return params


# Local Secondary Indexes still rely on the original Hash Key. When you supply a table with hash+range, think about
# the LSI as hash+range1, hash+range2.. hash+range6. You get 5 more range attributes to query on. Also, there is only
# one provisioned throughput.
def get_parameters_lsi(table_name):
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id', 'KeyType': 'HASH'},  # partition_key
            {'AttributeName': 'firstname', 'KeyType': 'RANGE'}  # sort_key
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'id', 'AttributeType': 'N'},
            {'AttributeName': 'firstname', 'AttributeType': 'S'},
            {'AttributeName': 'age', 'AttributeType': 'N'},
        ],
        'LocalSecondaryIndexes': [
            {
                'IndexName': 'EmployeeAge',
                'KeySchema': [
                    {'AttributeName': 'id', 'KeyType': 'HASH'},  # partition_key
                    {'AttributeName': 'age', 'KeyType': 'RANGE'}  # sort_key
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                }
            }
        ],

        'ProvisionedThroughput': {
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    }
    return params


# Global Secondary Indexes defines a new paradigm - different hash/range keys per index.
# This breaks the original usage of one hash key per table. This is also why when defining GSI
# you are required to add a provisioned throughput per index and pay for it.
def get_parameters_gsi(table_name):
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id', 'KeyType': 'HASH'},  # partition_key
            {'AttributeName': 'firstname', 'KeyType': 'RANGE'}  # sort_key
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'id', 'AttributeType': 'N'},
            {'AttributeName': 'firstname', 'AttributeType': 'S'},
            {'AttributeName': 'age', 'AttributeType': 'N'},
        ],
        'GlobalSecondaryIndexes': [
            {
                'IndexName': 'EmployeeAgeIndex',
                'KeySchema': [
                    {'AttributeName': 'age', 'KeyType': 'HASH'},  # partition_key
                    {'AttributeName': 'firstname', 'KeyType': 'RANGE'}  # sort_key
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 2,
                    'WriteCapacityUnits': 2
                }
            }
        ],

        'ProvisionedThroughput': {
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    }
    return params
