import boto3
from botocore.exceptions import ClientError
import logging
import subprocess
import os


def create_dynamo_local_context():
    try:
        try:
            log = os.getcwd()
            print('this is my dir',log)
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

        dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2', endpoint_url='http://localhost:8000')
        logging.info('Successfully return local context')
        return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response

