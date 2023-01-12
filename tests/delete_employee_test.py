from src import requests_module
from utils import fileReader
from utils.readProperties import ReadConfig


def test_delete_employee():

    data = fileReader.load_files('payload')
    _employee_name = data[0]['name']
    _employee_id = data[0]['id']
    params = {
        "name": _employee_name,
        "id": _employee_id
    }
    url = ReadConfig.get_employee_url()
    response = requests_module.delete_request(url, params=params, retries=3, retry_list=[500])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 202
    assert _response_msg == f"Successfully deleted Employee {_employee_name}"
    print(_response_msg)



