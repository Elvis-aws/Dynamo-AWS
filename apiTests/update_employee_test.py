from src import requests_module
from utils import fileReader, helpers
from utils.readProperties import ReadConfig


def test_update_employee():
    data = helpers.configure_update_employee_payload(17, 75)
    url = ReadConfig.get_employee_url()
    fileReader.write_files(payload=data, data_file='payload')
    response = requests_module.post_request(url, data=data, retries=3, retry_list=[500])
    _response_msg = response.text
    _employee_name = data[0]['name']
    _status_code = response.status_code
    assert _status_code == 200
    assert _response_msg == f"Successfully updated Employee: ['{_employee_name}']"
    print(_response_msg)


