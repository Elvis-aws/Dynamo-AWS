
# Run application
    # virtualenv env
    # source env/bin/activate
    # pip3 install -r requirements.txt
    # pip3 freeze > requirements.txt
    # Navigate to src/app
# On local env
    # set db = dynamo_context.create_dynamo_local_context()
    # export FLASK_APP=app.py
    # export FLASK_ENV=development
    # flask run
# On aws elasticbeanstalk env
    # create aws account
    # configure eb cli
    # set db = dynamo_context.create_dynamo_remote_context()
    # eb init
    # eb deploy
# Create table cli
    aws dynamodb create-table \
        --table-name EmployeeTable \
        --attribute-definitions \
            AttributeName=id,AttributeType=N \
            AttributeName=name,AttributeType=S \
        --key-schema AttributeName=id,KeyType=HASH AttributeName=name,KeyType=RANGE \
        --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
        --table-class STANDARD \
        --endpoint-url http://localhost:8000
# EB CLI
    Remove .elasticbeanstalk folder to reset eb init
    Commands
    eb abort
    eb appversion
    eb clone
    eb codesource
    eb config
    eb console
    eb create
    eb deploy
    eb events
    eb health
    eb init
    eb labs
    eb list
    eb local
    eb logs
    eb open
    eb platform
    eb printenv
    eb restore
    eb scale
    eb setenv
    eb ssh
    eb status
    eb swap
    eb tags
    eb terminate
    eb upgrade
    eb use