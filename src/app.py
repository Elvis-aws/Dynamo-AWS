from botocore.exceptions import ClientError
from flask import Flask, render_template, request, jsonify
from boto3.dynamodb.conditions import Key, Attr
from .config import dynamo_context, dynamoIndex, context
from datetime import date
app = Flask(__name__)

app.config.from_pyfile('config.py')
table_name = app.config.get('DYNAMODB_TABLE_NAME')
# gsi_lsi = str(dynamoIndex.DynamoIndexes.LOCALSECONDARYINDEX.value)
gsi_lsi = str(dynamoIndex.DynamoIndexes.GLOBALSECONDARYINDEX.value)

db = dynamo_context.create_dynamo_local_context(gsi_lsi)
# db = dynamo_context.create_dynamo_remote_context()


@app.route('/addEmployee', methods=['PUT'])
def add_employee():
    try:
        request_data = request.get_json()
        employee_names = []
        response = None
        if request.method == 'PUT':
            employee_table = db.Table(table_name)
            # Loop through the list of all employees
            for all_employees in request_data:
                employee_name = all_employees['firstname']
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
                app.logger.info(f'Employee successfully added {employee_name}')
        return jsonify(
            details="Successfully created Employees",
            server_response=response,
            statuscode=201,
            date=date.today(),
        )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/updateEmployee', methods=['POST'])
def update_employee():
    try:
        response = None
        request_data = request.get_json()
        employee_names = []
        if request.method == 'POST':
            employee_table = db.Table(table_name)

            for all_employees in request_data:
                employee_name = all_employees['firstname']
                employee_names.append(employee_name)
                employee_id = all_employees['id']
                employee_age = all_employees['age']
                employee_address = all_employees['address']
                employee_gender = all_employees['gender']
                employee_city = all_employees['city']
                employee_position = all_employees['profession']
                employee_status = all_employees['marital_status']
                employee_dob = all_employees['Date_of_birth']
                employee_list = employee_table.query(
                    KeyConditionExpression=Key('id').eq(employee_id))
                items = employee_list['Items']
                if len(items) == 0:
                    app.logger.info('Employee does not exist exist')
                    return f'Employee with ID: {employee_id} does not exist', 200
                response = employee_table.update_item(
                    Key={
                        'id': employee_id,
                        'firstname': employee_name
                    },
                    UpdateExpression="set age=:a,address=:d,gender=:g,city=:c,profession=:p,marital_status=:s,Date_of_birth=:o",
                    ExpressionAttributeValues={
                        ':a': employee_age,
                        ':d': employee_address,
                        ':g': employee_gender,
                        ':c': employee_city,
                        ':p': employee_position,
                        ':s': employee_status,
                        ':o': employee_dob
                    },

                    ReturnValues="UPDATED_NEW"

                )
                app.logger.info('Successfully updated employee')
        return jsonify(
            details=f"Successfully updated Employee: {employee_names}",
            server_response=response,
            date=date.today(),
        )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/scanEmployees', methods=['GET'])
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
                return jsonify(
                    details="The following employees exist in the Data base",
                    server_response=employee_list,
                    date=date.today(),
                )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


# Get only a particular set of attributes in our results
@app.route('/employeesAttribute', methods=['GET'])
def get_employees_by_attribute():
    try:
        projection_expression = 'firstname, id, city, Date_of_birth, age'
        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            employee_list = employee_table.scan(
                ProjectionExpression=projection_expression
            )
            if employee_list['Count'] == 0:
                return f"There are no Employees in the Data Base", 200
            else:
                return jsonify(
                    details="The following employees exist in the Data base",
                    server_response=employee_list,
                    date=date.today(),
                )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/filterEmployees', methods=['GET'])
def get_employees_by_filter():
    try:
        filter_expression = 'city'
        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            employee_list = employee_table.scan(
                FilterExpression=Attr(filter_expression).begins_with('A'),
                # Define the maximum number of items to be returned
                Limit=7
            )
            if employee_list['Count'] == 0:
                return f"There are no Employees in the Data Base", 200
            else:
                return jsonify(
                    details="The following employees exist in the Data base",
                    server_response=employee_list,
                    date=date.today(),
                )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/paginationEmployees', methods=['GET'])
def get_employees_by_pagination():
    try:
        # Track number of Items read
        item_count = 0

        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            response = employee_table.scan(
                Select="ALL_ATTRIBUTES"
            )
            item_count += len(response['Items'])

            # Paginate returning up to 1MB of data for each iteration
            while 'LastEvaluatedKey' in response:
                response = employee_table.scan(
                    ExclusiveStartKey=response['LastEvaluatedKey']
                )
                # Track number of Items read
                item_count += len(response['Items'])

            if item_count == 0:
                return f"There are no Employees in the Data Base", 200
            else:
                return jsonify(
                    details="The following employees exist in the Data base",
                    employees=response['Items'],
                    statuscode=200,
                    date=date.today(),
                )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/getEmployee', methods=['GET'])
def get_employee():
    try:
        request_data_id = request.args.get('id')
        request_data_name = request.args.get('firstname')
        request_data_age = request.args.get('age')
        if request.method == 'GET':
            employee_table = db.Table(table_name)

            # Loop through all the items and load each
            employee_list = employee_table.query(
                # This query does not take into account LSI or GSI
                # KeyConditionExpression=Key('id').eq(int(request_data_id)) & Key('firstname').eq(request_data_name)

                # Here providing the index name queries with respect to the LSI
                # IndexName='EmployeeAge',
                # KeyConditionExpression=Key('id').eq(int(request_data_id)) & Key('age').eq(int(request_data_age))

                # Using a query with GSI is as if you are using a new table
                IndexName='EmployeeAgeIndex',
                KeyConditionExpression=Key('age').eq(int(request_data_age)) & Key('firstname').eq(request_data_name)
            )
            if employee_list['Count'] == 0:
                return f"No Employee with id and name : {request_data_id}: {request_data_name}", 200
            else:
                app.logger.info('Successfully retrieved employee')
                return jsonify(
                    details="Successfully retrieved Employee",
                    server_response=employee_list,
                    date=date.today(),
                    statusCode=200
                )
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/index', methods=['GET'])
def get_html():
    try:
        if request.method == 'GET':
            return render_template('index.html')
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/healthcheck', methods=['GET'])
def get_health_status():
    return jsonify(
        details="Application is in OK State",
        date=date.today(),
        statusCode=200
    )


@app.route('/deleteTable', methods=['DELETE'])
def delete_table():
    try:
        table_names = [table.name for table in db.tables.all()]
        if table_name in table_names:
            table = db.Table(table_name)
            table.delete()
            table.wait_until_not_exists()
            app.logger.info(f'Successfully deleted Table: {table_name}')
            return f'Successfully deleted Table: {table_name}'
        else:
            app.logger.info(f'Table: {table_name} does not exist')
            return f'Table: {table_name} does not exist'
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/create_table', methods=['GET'])
def create_table():
    try:
        table_names = [table.name for table in db.tables.all()]
        if table_name in table_names:
            app.logger.info(f'Table: {table_name} already exist')
            return f'Table: {table_name} already exist'
        else:
            dynamo_context.create_dynamo_local_context(context.Context.indexes)
            # db = dynamo_context.create_dynamo_remote_context()
            app.logger.info(f'Successfully created Table: {table_name}')
            return f'Successfully created Table: {table_name}'
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


@app.route('/deleteEmployee', methods=['DELETE'])
def delete_employee():
    try:
        request_data_name = request.args.get('firstname')
        request_data_id = int(request.args.get('id'))
        if request.method == 'DELETE':
            employee_table = db.Table(table_name)

            employee_list = employee_table.query(
                KeyConditionExpression=Key('id').eq(request_data_id))
            items = employee_list['Items']
            if len(items) == 0:
                app.logger.info(f'No employees exist with id: {request_data_id}')
                return f'No employees exist with id: {request_data_id}', 200
            for employee in employee_list['Items']:
                if employee['id'] == int(request_data_id) and employee['firstname'] == request_data_name:
                    response = employee_table.delete_item(
                        Key={
                            'firstname': request_data_name,
                            'id': request_data_id
                        }
                    )
                    app.logger.info('Successfully deleted employee')
                    return jsonify(
                        details="Successfully deleted Employee",
                        server_response=response,
                        date=date.today(),
                        statusCode=202
                    )
                else:
                    return f"No employee exist with id: {employee['id']} and name: {employee['firstname']} combination", 200
    except ClientError as ex:
        app.logger.critical(ex.response)
        return ex.response


if __name__ == '__main__':
    # export FLASK_APP=src/app.py
    # export FLASK_ENV=development
    # flask run
    app.run(debug=True, host='0.0.0.0')
