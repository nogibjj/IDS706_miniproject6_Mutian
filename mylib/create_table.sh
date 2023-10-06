#!/bin/bash

# 定义表的名称
table_name="MyTable"

# 定义主键架构
key_schema='[
    {"AttributeName": "UserID", "KeyType": "HASH"},
    {"AttributeName": "Username", "KeyType": "RANGE"}
]'

# 定义属性定义
attribute_definitions='[
    {"AttributeName": "UserID", "AttributeType": "S"},
    {"AttributeName": "Username", "AttributeType": "S"},
      {"AttributeName": "Age", "AttributeType": "N"}
]'

# 定义吞吐量配置
read_capacity_units=5
write_capacity_units=5

# 使用AWS CLI创建DynamoDB表
aws dynamodb create-table \
    --table-name "$table_name" \
    --key-schema "$key_schema" \
    --attribute-definitions "$attribute_definitions" \
    --provisioned-throughput "ReadCapacityUnits=$read_capacity_units,WriteCapacityUnits=$write_capacity_units"\
    --global-secondary-indexes \
        "[{
            \"IndexName\": \"AgeIndex\",
            \"KeySchema\": [
                {\"AttributeName\": \"Age\",\"KeyType\": \"HASH\"}
            ],
            \"Projection\": {
                \"ProjectionType\": \"ALL\"
            },
            \"ProvisionedThroughput\": {
                \"ReadCapacityUnits\": 5,
                \"WriteCapacityUnits\": 5
            }

        }]"
