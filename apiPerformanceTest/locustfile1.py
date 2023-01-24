from locust import SequentialTaskSet, task, tag, HttpUser, between
import logging


class EmployeeTest(SequentialTaskSet):
    @task
    @tag('emp')
    def get_employee(self):
        with self.client.get("?id=70&name=Marion", catch_response=True) as response:
            if response.status_code == 200 and ("Successfully retrieved Employee" in response.text):
                response.success()
            else:
                logging.error(response)
                response.failure("Get employee Test failed")

    @task
    @tag('emp')
    def get_employee_response_time(self):
        with self.client.get("?id=70&name=Marion", catch_response=True) as response:
            if response.status_code == 200 and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                logging.error(response)
                response.failure("Get employee response time Test failed")

    def on_stop(self):
        self.client.cookies.clear()


class EmployeesTest(SequentialTaskSet):

    @task
    @tag('emps')
    def get_all_employees(self):
        with self.client.get("/allEmployees", catch_response=True) as response:
            if response.status_code == 200 and ("The following employees exist in the Data base" in response.text):
                response.success()
            else:
                logging.error(response)
                response.failure("Get all employee test failed")

    @task
    @tag('emps')
    def get_all_employees_response_time(self):
        with self.client.get("/allEmployees", catch_response=True) as response:
            if response.status_code == 200 and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                logging.error(response)
                response.failure("Get all employee response time test failed")

    def on_stop(self):
        self.client.cookies.clear()


class TestRunnerEmployee(HttpUser):
    # wait_time = constant(1)
    wait_time = between(0.05, 0.1)
    # Make request to endpoint
    host = "http://127.0.0.1:9002/Employee"
    # Tasks to execute which is the test class above
    tasks = [EmployeeTest]


class TestRunnerEmployees(HttpUser):
    # wait_time = constant(1)
    wait_time = between(0.05, 0.1)
    # Make request to endpoint
    host = "http://127.0.0.1:9002/Employee"
    # Tasks to execute which is the test class above
    tasks = [EmployeesTest]
