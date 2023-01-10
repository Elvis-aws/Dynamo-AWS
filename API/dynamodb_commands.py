
# docker-compose up -d
# aws sts get-caller-identity
# ps aux | grep dynamodb
# aws dynamodb list-tables --endpoint-url http://localhost:8000
# aws dynamodb describe-table --table-name employeeTable --endpoint-url http://localhost:8000
# aws dynamodb scan --table-name employeeTable --endpoint-url http://localhost:8000
"""
aws dynamodb describe-table \
    --table-name employeeTable
"""

"""
aws dynamodb scan \
    --table-name employeeTable
    --endpoint-url http://localhost:8000
"""

"""
aws dynamodb get-item \
    --table-name employeeTable \
    --key '{"id": {"S": "123"}, "email": {"S": "john@doe.com"}}'
    --consistent-read # This is optional
    --endpoint-url http://localhost:8000

"""

"""
aws dynamodb scan \
    --table-name employeeTable
    --filter-expression "lastName = :name" \
    --expression-attribute-values '{":name":{"S":"Doe"}}'
    --endpoint-url http://localhost:8000

"""

"""
aws dynamodb scan \
    --table-name employeeTable \
    --filter-expression "lastName = :lastName" \
    --projection-expression "#AA, #BB" \
    --expression-attribute-names file://expression-attribute-names.json \
    --expression-attribute-values file://expression-attribute-values.json
    --endpoint-url http://localhost:8000

"""

"""
aws dynamodb get-item \
    --table-name employeeTable \
    --key '{"id": {"S": "123"}, "email": {"S": "john@doe.com"}}'
    --consistent-read # This is optional
    --endpoint-url http://localhost:8000
"""

"""
aws dynamodb query \
    --table-name employeeTable \
    --key-condition-expression "id = :myId" \
    --expression-attribute-values '{":v1": {"S": "Fire Walk With Me"}}'
    --endpoint-url http://localhost:8000
"""

"""
aws dynamodb query \
    --table-name employeeTable \
    --key-condition-expression "id = :myId" \
    --expression-attribute-values '{":v1": {"S": "Fire Walk With Me"}}'
    --filter-expression 'attribute_not_exists(updatedAt)'
    --endpoint-url http://localhost:8000
"""

"""
aws dynamodb query \
    --table-name employeeTable \
    --key-condition-expression "id = :myId" \
    --expression-attribute-values '{":v1": {"S": "Fire Walk With Me"}}'
    --filter-expression 'attribute_not_exists(updatedAt)'
    --scan-index-forward
    --endpoint-url http://localhost:8000
"""

"""
aws dynamodb query \
    --table-name employeeTable \
    --key-condition-expression "id = :myId" \
    --expression-attribute-values '{":v1": {"S": "Fire Walk With Me"}}'
    --filter-expression 'attribute_not_exists(updatedAt)'
    --scan-index-forward
    --starting-token '<VALUE_OF_NEXT_TOKEN_FROM_PREV_OPERATION>'
    --endpoint-url http://localhost:8000
"""
