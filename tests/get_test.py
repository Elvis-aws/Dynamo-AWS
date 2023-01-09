from src import requests_module


def test_verify_status_code():
    params = {'AuthorName': 'Elvis'}
    headers = {"Content-Type": "json"}
    url = 'http://216.10.245.166/Library/GetBook.php'

    response = requests_module.get_request(url, **params, **headers, retries=3, retry_list=[500])
    _status_code = response.status_code
    assert _status_code == 200
