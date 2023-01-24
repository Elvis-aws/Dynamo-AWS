from locust import SequentialTaskSet, task, tag, HttpUser, between
from utils import helpers, fileReader


class CreateDeleteEmployeeTest(SequentialTaskSet):

    @task
    @tag('emp')
    def create_employee(self):
        _data = helpers.configure_update_employee_payload(17, 75)
        with self.client.put(data=_data, retries=3, retry_list=[500], catch_response=True) as response:
            if response.status_code == 200 and ("Successfully retrieved Employee" in response.text):
                response.success()
            else:
                response.failure("Test failed")

    @task
    @tag('emp')
    def get_employee_response_time(self):
        params = helpers.employee_params()
        with self.client.get(f"?id={params['id']}&name={params['name']}", retries=3, retry_list=[500], catch_response=True) as response:
            if response.status_code == 200 and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                response.failure("Test failed")

    @task
    @tag('emp')
    def update_employee_response_time(self):
        data = helpers.configure_update_employee_payload(17, 75)
        fileReader.write_files(payload=data, data_file='payload')
        with self.client.update(data=data, retries=3, retry_list=[500],
                                catch_response=True) as response:
            if response.status_code == 200 and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                response.failure("Test failed")

    @task
    @tag('emp')
    def delete_employee_response_time(self):
        params = helpers.employee_params()
        with self.client.delete(f"?id={params['id']}&name={params['name']}", retries=3, retry_list=[500],
                                catch_response=True) as response:
            if response.status_code == 200 and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                response.failure("Test failed")

    def on_stop(self):
        self.client.cookies.clear()


class TestRunnerEmployee(HttpUser):
    # wait_time = constant(1)
    wait_time = between(0.05, 0.1)
    # Make request to endpoint
    host = "http://127.0.0.1:9002/Employee"
    # Tasks to execute which is the test class above
    tasks = [CreateDeleteEmployeeTest]
