import requests
from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter, Retry
from utils.rapper_function import func_loger

session = requests.Session()


@func_loger
def get_request(url, params=None, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        retry = __configure_retires(retries=retries, retry_list=retry_list)
        session.mount('http://', HTTPAdapter(max_retries=retry))
        response = session.get(url=url, params=params, headers=kwargs, timeout=timeout)
        return response

    except HTTPError as http_error:
        return http_error

    except Exception as error:
        return error


@func_loger
def delete_request(url, params, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        retry = __configure_retires(retries=retries, retry_list=retry_list)
        session.mount('http://', HTTPAdapter(max_retries=retry))
        response = session.delete(url=url, params=params, headers=kwargs, timeout=timeout)
        return response
    except HTTPError as http_error:
        return http_error
    except Exception as error:
        return error


@func_loger
def post_request(url, data, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        retry = __configure_retires(retries=retries, retry_list=retry_list)
        session.mount('http://', HTTPAdapter(max_retries=retry))
        response = session.post(url=url, json=data, params=kwargs, headers=kwargs, timeout=timeout)
        return response

    except HTTPError as http_error:
        return http_error
    except Exception as error:
        return error


@func_loger
def put_request(url, data, timeout=None, retries: int = None, retry_list: list = None, **kwargs):
    try:
        retry = __configure_retires(retries=retries, retry_list=retry_list)
        session.mount('http://', HTTPAdapter(max_retries=retry))
        response = session.put(url=url, json=data, params=kwargs, headers=kwargs, timeout=timeout)
        return response
    except HTTPError as http_error:
        return http_error
    except Exception as error:
        return error


@func_loger
def __configure_retires(retries: int, retry_list: list):
    retries = Retry(total=retries,
                    backoff_factor=0.1,
                    status_forcelist=retry_list)
    return retries
