import boto3
from botocore.exceptions import ClientError
import logging
from .dynamo_params import *
from .dynamoIndex import DynamoIndexes
from .context import Context
table_name = 'EmployeeTable'


def create_dynamo_remote_context():
    try:
        dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2')
        logging.info('Successfully return local context')
        return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response


def create_dynamo_local_context(indexes: str):
    try:
        Context.indexes = indexes
        dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url='http://localhost:8000')
        print("Connecting to local dynamoDB")
        logging.info("Connecting to local dynamoDB")
        # Append any existing tables to the dynamoDB_tables list
        table_names = [table.name for table in dyn_resource.tables.all()]
        if table_name in table_names:
            print(f"Table {table_name} already exist")
            logging.info(f"Table {table_name} already exist")
            return dyn_resource
        elif indexes == DynamoIndexes.LOCALSECONDARYINDEX.value:
            # Create table with LSI
            params = get_parameters_lsi(table_name=table_name)
            table = dyn_resource.create_table(**params)
            print(f"Creating LSI table:{table_name}...")
            logging.info(f"Creating lsi {table_name}...")
            table.wait_until_exists()
            print(f"LSI {table_name} creation complete")
            logging.info(f"LSI {table_name} creation complete")
            return dyn_resource
        elif indexes == DynamoIndexes.GLOBALSECONDARYINDEX.value:
            # Create table with GSI
            params = get_parameters_gsi(table_name=table_name)
            table = dyn_resource.create_table(**params)
            print(f"Creating gsi table:{table_name}...")
            logging.info(f"Creating gsi table: {table_name}...")
            table.wait_until_exists()
            print(f"Table {table_name} creation complete")
            logging.info(f"Table {table_name} creation complete")
            return dyn_resource
        else:
            # Create table with None
            params = get_parameters(table_name=table_name)
            table = dyn_resource.create_table(**params)
            print(f"Creating {table_name}...")
            logging.info(f"Creating {table_name}...")
            table.wait_until_exists()
            print(f"Table {table_name} creation complete")
            logging.info(f"Table {table_name} creation complete")
            return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response
