import random

import random_address

from src import requests_module
from utils import fileReader
from utils.fileReader import load_files
from utils.readProperties import ReadConfig
from utils.gender import get_gender


def test_update_employee():
    """get employee id and name to update"""
    _data = load_files('payload')
    _employee_id = _data[0]['id']
    _employee_name = _data[0]['name']
    """update employee details"""
    _random_address = random_address.real_random_address()
    _employee_address = _random_address['address1']
    _employee_age = random.randint(17, 75)
    _gender = get_gender()
    fileReader.update_json_file(_file_name='update_payload', _id=_employee_id, _name=_employee_name, _address=_employee_address, _age=_employee_age, _gender=_gender)

    data = fileReader.load_files('update_payload')
    url = ReadConfig.get_employee_url()
    fileReader.write_files(payload=data, data_file='payload')
    response = requests_module.post_request(url, data=data, retries=3, retry_list=[500])
    _response_msg = response.text
    _employee_name = data[0]['name']
    _status_code = response.status_code
    assert _status_code == 200
    assert _response_msg == f"Successfully updated Employee: ['{_employee_name}']"
    print(_response_msg)


