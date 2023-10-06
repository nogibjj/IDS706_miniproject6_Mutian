"""
Implements identical example the CLI in Python

# DynamoDB Demos

## CLI Demo

### Create Table

```bash
aws dynamodb create-table \
    --table-name customers \
    --attribute-definitions \
        AttributeName=customer_id,AttributeType=N \
    --key-schema \
        AttributeName=customer_id,KeyType=HASH \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5
```

### List Tables

```bash
aws dynamodb list-tables
```

### Put Item

```bash
aws dynamodb put-item \
    --table-name customers \
    --item \
        '{"customer_id": {"N": "1"}, "name": {"S": "John Doe"}}'
```

### Get Item

```bash
aws dynamodb get-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}'
```

### Update Item

```bash
aws dynamodb update-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}' \
    --update-expression \
        "SET #name = :name" \
    --expression-attribute-names \
        '{"#name": "name"}' \
    --expression-attribute-values \
        '{":name": {"S": "Jane Doe"}}'
```

### Query Items

```bash
aws dynamodb query \
    --table-name customers \
    --key-condition-expression \
        "customer_id = :customer_id" \
    --expression-attribute-values \
        '{":customer_id": {"N": "1"}}'
```

### Scan Items

```bash
aws dynamodb scan \
    --table-name customers
```

### Delete Item

```bash
aws dynamodb delete-item \
    --table-name customers \
    --key \
        '{"customer_id": {"N": "1"}}'
```

### Delete Table

```bash
aws dynamodb delete-table \
    --table-name customers
```
"""

import boto3
from boto3.dynamodb.conditions import Key

def list_tables(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    return dynamodb.tables.all()


def put_item(userid,name,age,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")
    response = table.put_item(Item={"UserID": userid, "Username": name,"Age":age})

    return response


def get_item(userid,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")
    response = table.get_item(Key={"UserID": userid})

    return response


def update_item(userid,username,dynamodb=None):
    """Updates the name for UserID = userid to username"""

    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")

    response = table.update_item(
        Key={"UserID": userid},
        UpdateExpression="SET #name = :new_name",
        ExpressionAttributeNames={"#name": "Username"},
        ExpressionAttributeValues={":new_name": username},
        ReturnValues="UPDATED_NEW",
    )
    return response


def query_items(userid,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")

    response = table.query(KeyConditionExpression=Key("UserID").eq(userid))

    return response


def scan_items(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")
    response = table.scan()

    return response


def delete_item(userid,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")
    response = table.delete_item(Key={"UserID": userid})

    return response


def delete_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("MyTable")
    table.delete()

    return table
