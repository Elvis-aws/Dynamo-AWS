from src import requests_module
from utils import fileReader
from utils.readProperties import ReadConfig


def test_get_employee():

    data = fileReader.load_files('payload')
    _employee_name = data[0]['name']
    _employee_id = data[0]['id']
    _employee_age = data[0]['age']
    _employee_address = data[0]['address']
    _employee_gender = data[0]['gender']
    params = {
        "id": _employee_id,
        "name": _employee_name
    }
    url = ReadConfig.get_employee_url()

    response = requests_module.get_request(url, params=params, retries=3, retry_list=[500])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 200
    assert str(_employee_id) in _response_msg
    assert _employee_name in _response_msg
    assert str(_employee_age) in _response_msg
    assert _employee_address in _response_msg
    assert _employee_gender in _response_msg
    print(_response_msg)


def test_get_all_employees():
    url = ReadConfig.get_all_employee_url()

    response = requests_module.get_request(url, retries=3, retry_list=[500, 400])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 200
    assert 'Items' in _response_msg
    print(_response_msg)


