import boto3
from botocore.exceptions import ClientError
import logging


def create_dynamo_remote_context():
    try:
        dyn_resource = boto3.resource('dynamodb', region_name='eu-west-2')
        logging.info('Successfully return local context')
        return dyn_resource
    except ClientError as ex:
        logging.error(f'An error occurred {ex.response}')
        raise ex.response
