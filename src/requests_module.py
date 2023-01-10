import requests
from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter, Retry
from utils import api_logger

session = requests.Session()
logger = api_logger.loggen()


def get_request(url, params=None, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        logger.info('Configuring retry')
        retry = __configure_retires(retries=retries, retry_list=retry_list)

        logger.info('Mounting session retry')
        session.mount('http://', HTTPAdapter(max_retries=retry))

        logger.info('Executing get request')
        response = session.get(url=url, params=params, headers=kwargs, timeout=timeout)
        logger.info('Request successful')
        return response

    except HTTPError as http_error:
        logger.error('Request un-successful with http-error')
        return http_error

    except Exception as error:
        logger.error('Request un-successful with exception')
        return error


def delete_request(url, params, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        logger.info('Configuring retry')
        retry = __configure_retires(retries=retries, retry_list=retry_list)

        logger.info('Mounting session retry')
        session.mount('http://', HTTPAdapter(max_retries=retry))

        logger.info('Executing get request')
        response = session.delete(url=url, params=params, headers=kwargs, timeout=timeout)
        logger.info('Request successful')
        return response

    except HTTPError as http_error:
        logger.error('Request un-successful with http-error')
        return http_error

    except Exception as error:
        logger.error('Request un-successful with exception')
        return error


def post_request(url, data, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        logger.info('Configuring retry')
        retry = __configure_retires(retries=retries, retry_list=retry_list)

        logger.info('Mounting session retry')
        session.mount('http://', HTTPAdapter(max_retries=retry))

        logger.info('Executing post request')
        response = session.post(url=url, json=data, params=kwargs, headers=kwargs, timeout=timeout)
        logger.info('Request successful')
        return response

    except HTTPError as http_error:
        logger.error('Request un-successful with http-error')
        return http_error

    except Exception as error:
        logger.error('Request un-successful with exception')
        return error


def put_request(url, data, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        logger.info('Configuring retry')
        retry = __configure_retires(retries=retries, retry_list=retry_list)

        logger.info('Mounting session retry')
        session.mount('http://', HTTPAdapter(max_retries=retry))

        logger.info('Executing put request')
        response = session.put(url=url, json=data, params=kwargs, headers=kwargs, timeout=timeout)
        logger.info('Request successful')
        return response

    except HTTPError as http_error:
        logger.error('Request un-successful with http-error')
        return http_error

    except Exception as error:
        logger.error('Request un-successful with exception')
        return error


def __configure_retires(retries: int, retry_list: list):
    retries = Retry(total=retries,
                    backoff_factor=0.1,
                    status_forcelist=retry_list)
    return retries
