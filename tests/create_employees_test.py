from src import requests_module
import names
import random_address
from utils.fileReader import load_files, update_json_file
import random

from utils.readProperties import ReadConfig


def test_create_new_employees():
    """getting and incrementing employee id"""
    _data = load_files('payload')
    _employee_id = _data[0]['id']
    _new_employee_id = _employee_id + 1
    """generating random name"""
    _new_employee_name = names.get_first_name()
    """generating random address"""
    _new_random_address = random_address.real_random_address()
    _new_employee_address = _new_random_address['address1']
    """generating random age"""
    _new_employee_age = random.randint(17, 75)

    _data = update_json_file('payload', _id=_new_employee_id, _name=_new_employee_name,
                             _address=_new_employee_address, _gender='Male', _age=_new_employee_age)
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
