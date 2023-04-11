from request import requests_module
from utils import helpers
from utils.readProperties import ReadConfig


def test_get_employee():
    employee_details = helpers.get_employee_details_from_payload()
    params = helpers.employee_params()
    url = ReadConfig.get_employee_url()
    response = requests_module.get_request(url, params=params, retries=3, retry_list=[500])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 200
    assert str(employee_details['id']) in _response_msg
    assert employee_details['name'] in _response_msg
    assert str(employee_details['age']) in _response_msg
    assert employee_details['address'] in _response_msg
    assert employee_details['gender'] in _response_msg
    print(_response_msg)


def test_get_all_employees():
    url = ReadConfig.get_all_employee_url()
    response = requests_module.get_request(url, retries=3, retry_list=[500, 400])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 200
    assert 'Items' in _response_msg
    print(_response_msg)


