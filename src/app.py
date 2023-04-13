from botocore.exceptions import ClientError
from flask import Flask, render_template, request
from boto3.dynamodb.conditions import Key
from .config import dynamo_context

app = Flask(__name__)

app.config.from_pyfile('config.py')
table_name = app.config.get('DYNAMODB_TABLE_NAME')
# db = dynamo_context.create_dynamo_local_context()
db = dynamo_context.create_dynamo_remote_context()


@app.route('/Employee', methods=['PUT'])
def create_employee():
    try:
        request_data = request.get_json()
        employee_names = []
        if request.method == 'PUT':
            employee_table = db.Table(table_name)
            # Loop through the list of all employees
            for all_employees in request_data:
                employee_name = all_employees['name']
                employee_names.append(employee_name)
                employee_id = all_employees['id']
                employee_list = employee_table.query(
                    KeyConditionExpression=Key('id').eq(employee_id))
                items = employee_list['Items']
                if len(items) != 0:
                    emp_id = items[0]['id']
                    if employee_id == emp_id:
                        app.logger.info('Employee already exist')
                        return f'Employee with ID: {employee_id} already exist', 409
                response = employee_table.put_item(Item=all_employees)
                app.logger.info('Employee successfully added')

        return f'Successfully created Employees: {employee_names}', 201
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/Employee', methods=['POST'])
def update_employee():
    try:
        request_data = request.get_json()
        employee_names = []
        if request.method == 'POST':
            employee_table = db.Table(table_name)

            for all_employees in request_data:
                employee_name = all_employees['name']
                employee_names.append(employee_name)
                employee_id = all_employees['id']
                employee_age = all_employees['age']
                employee_address = all_employees['address']
                employee_gender = all_employees['gender']
                employee_list = employee_table.query(
                    KeyConditionExpression=Key('id').eq(employee_id))
                items = employee_list['Items']
                if len(items) == 0:
                    app.logger.info('Employee does not exist exist')
                    return f'Employee with ID: {employee_id} does not exist', 200
                response = employee_table.update_item(
                    Key={
                        'id': employee_id,
                        'name': employee_name
                    },
                    UpdateExpression="set age=:a,address=:d,gender=:g",
                    ExpressionAttributeValues={
                        ':a': employee_age,
                        ':d': employee_address,
                        ':g': employee_gender

                    },

                    ReturnValues="UPDATED_NEW"

                )
                app.logger.info('Successfully updated employee')
        return f'Successfully updated Employee: {employee_names}', 200
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/Employee/allEmployees', methods=['GET'])
def get_employees():
    try:
        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            employee_list = employee_table.scan(
                Select="ALL_ATTRIBUTES"
            )
            if employee_list['Count'] == 0:
                return f"There are no Employees in the Data Base", 200
            else:
                return f"The following employees exist in the Data base: {employee_list}", 200
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/Employee', methods=['GET'])
def get_employee():
    try:
        request_data_id = request.args.get('id')
        request_data_name = request.args.get('name')
        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            employee_list = employee_table.query(
                KeyConditionExpression=Key('id').eq(int(request_data_id))
            )
            if employee_list['Count'] == 0:
                return f"There is no Employee in the Data Base with name: {request_data_name}", 200
            else:
                for employee in employee_list['Items']:
                    if employee['id'] == int(request_data_id):
                        app.logger.info('Successfully retrieved employee')
                        return f'Successfully retrieved Employee: {employee}'
                    else:
                        return f"No employee exist with name: {employee['name']}", 200
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/Employee/index', methods=['GET'])
def get_html():
    try:
        if request.method == 'GET':
            return render_template('index.html')
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/healthcheck', methods=['GET'])
def get_health_status():
    return 'Application is in OK State'


@app.route('/Employee', methods=['DELETE'])
def delete_employee():
    try:
        request_data_name = request.args.get('name')
        request_data_id = int(request.args.get('id'))
        if request.method == 'DELETE':
            employee_table = db.Table(table_name)

            employee_list = employee_table.query(
                KeyConditionExpression=Key('id').eq(request_data_id))
            items = employee_list['Items']
            if len(items) == 0:
                app.logger.info(f'No employees exist with id: {request_data_id}')
                return f'No employees exist with id: {request_data_id}', 200

            response = employee_table.delete_item(
                Key={
                    'name': request_data_name,
                    'id': request_data_id
                }
            )
            app.logger.info('Successfully deleted employee')
            return f'Successfully deleted Employee {request_data_name}', 202
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


if __name__ == '__main__':
    # export FLASK_APP=app.py
    # export FLASK_ENV=development
    # flask run
    app.run(debug=True, host='0.0.0.0')
