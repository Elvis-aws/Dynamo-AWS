from src import requests_module
from utils.fileReader import load_files
from utils import helpers
from utils.readProperties import ReadConfig


def test_create_new_employees():
    _data = helpers.configure_create_employee_payload(17, 75)
    url = ReadConfig.get_employee_url()
    response = requests_module.put_request(url, data=_data, retries=3, retry_list=[500])
    _response_msg = response.text
    _employee_name_One = _data[0]['name']
    _status_code = response.status_code
    assert _status_code == 201
    assert _response_msg == f"Successfully created Employees: ['{_employee_name_One}']"
    print(_response_msg)


def test_verify_employees_exist():
    data = load_files('payload')
    url = ReadConfig.get_employee_url()
    response = requests_module.put_request(url, data=data, retries=3, retry_list=[500])
    _response_msg = response.text
    _employee_id_One = data[0]['id']
    _status_code = response.status_code
    assert _status_code == 409
    assert _response_msg == f"Employee with ID: {_employee_id_One} already exist"
    print(_response_msg)
