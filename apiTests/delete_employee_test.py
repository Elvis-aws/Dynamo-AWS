from request import requests_module
from utils import helpers
from utils.readProperties import ReadConfig


def test_delete_employee():
    params = helpers.employee_params()
    url = ReadConfig.get_employee_url()
    response = requests_module.delete_request(url, params=params, retries=3, retry_list=[500])
    _response_msg = response.text
    _status_code = response.status_code
    assert _status_code == 202
    assert _response_msg == f"Successfully deleted Employee {params['name']}"
    print(_response_msg)



