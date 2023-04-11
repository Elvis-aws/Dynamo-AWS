import boto3
from botocore.exceptions import ClientError
import logging
import subprocess
import os

DYNAMODB_TABLE_NAME = 'EmployeeTable'


def create_dynamo_remote_context():
    try:
        dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2')
        logging.info('Successfully return local context')
        return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response


def create_dynamo_local_context():
    try:
        try:
            log = os.getcwd()
            log_dir = log + '/dynamodb_local_latest/'
            # change directory to the desired folder
            folder_path = log_dir
            command = 'cd ' + folder_path + ' && java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb'
            # open a shell and run the command
            process = subprocess.Popen(command, shell=True)

        except IOError as io:
            print(io)
            pass
        except Exception as ex:
            raise ex

        dyn_resource = boto3.resource('dynamodb',  endpoint_url='http://localhost:8000', region_name='eu-west-2')
        logging.info('Successfully return local context')
        return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response


DYNAMODB_AWS = create_dynamo_remote_context()
DYNAMODB_CONTEXT = create_dynamo_local_context()
