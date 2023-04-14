import pytest


@pytest.mark.smoke
def test_index_route_status_code_200():
    pass


@pytest.mark.smoke
def test_index_route_text():
    pass


@pytest.mark.smoke
def test_one():
    assert True


@pytest.mark.smoke
def test_two():
    assert True


@pytest.mark.smoke
def test_three():
    assert True


@pytest.mark.smoke
def test_eval_addition():
    assert eval("2 + 2") == 4


@pytest.mark.smoke
def test_eval_subtraction():
    assert eval("2 - 2") == 0


@pytest.mark.regression
def test_eval_multiplication():
    assert eval("2 * 2") == 4


@pytest.mark.regression
def test_eval_division():
    assert eval("2 / 2") == 1.0


@pytest.mark.regression
def test_index_route_status_code_500():
    pass


if __name__ == '__main__':
    pass
