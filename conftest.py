import pytest
from utils.context import Context
from pytest_harvest import saved_fixture


# For test initialization
@pytest.fixture(autouse=True)
@saved_fixture  # to save all instances created. access using fixture_store
def setup():

    # post test execution
    message = 'Hello api test automation'
    Context.message = message

    yield

    # post test execution

