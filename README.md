# Python-API-Framework


# Create virtual env
- virtualenv env
- source env/bin/activate
# Run application
    # source env/bin/bin/bin/activate 
    # cd API
    # pip3 install -r requirements.txt
    # pip3 freeze > requirements.txt
    # docker-compose up -d
    # python3 application.py


# Deploy to Elastic beanstalk
    # Rename main file to application.py
    # Rename flask app to application
    # Create requirements file
    # Create .ebextensions folder

# EB CLI
    Remove .elasticbeanstalk folder to reset eb init
    pip3 install awsebcli
    virtual environment
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