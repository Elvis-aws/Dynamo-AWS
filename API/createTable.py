import boto3
from context import Context
from botocore.exceptions import ClientError
local_dynamodb = False


def create_dax_table(table_name, dyn_resource=None):
    """
    Creates a DynamoDB table.

    param dyn_resource: Either a Boto3 or DAX resource.
    :return: The newly created table.
    """
    # endpoint_url='http://localhost:8000'
    try:
        dax_table_context = []
        all_tables = []
        if dyn_resource is None:
            if local_dynamodb is True:
                dyn_resource = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
                Context.dynamodb_local = dyn_resource
            else:
                dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2')
                Context.dynamodb_local = dyn_resource
            for table in dyn_resource.tables.all():
                all_tables.append(table.name)
            if table_name in all_tables:
                print(f"Table {table_name} already exist")
                dax_table_context.append({"name": table.name})
                dax_table_context.append({"id": table.table_id})
                dax_table_context.append({"status": table.table_status})
                Context.dynamodb_table = table.name
                return dax_table_context

        table_name = table_name
        params = {
            'TableName': table_name,
            'KeySchema': [
                {'AttributeName': 'id', 'KeyType': 'HASH'},  # partition_key
                {'AttributeName': 'name', 'KeyType': 'RANGE'}  # sort_key
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'id', 'AttributeType': 'N'},
                {'AttributeName': 'name', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 2,
                'WriteCapacityUnits': 2
            }
        }
        table = dyn_resource.create_table(**params)
        print(f"Creating {table_name}...")
        table.wait_until_exists()
        dax_table_context.append({"name": table.name})
        dax_table_context.append({"id": table.table_id})
        dax_table_context.append({"status": table.table_status})
        Context.dynamodb_table = table_name
        print(f"Table {table_name} creating complete")
    except ClientError as ex:
        return ex.response
    return dax_table_context
