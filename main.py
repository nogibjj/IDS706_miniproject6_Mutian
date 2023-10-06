from mylib.dynamodb import (
    list_tables,
    delete_item,
    delete_table,
    get_item,
    scan_items,
    put_item,
    update_item,
    query_items,
)

import boto3
import random
import string

# insert some data to the table
def inserdata():
    dynamodb = boto3.client("dynamodb")

    table_name = "MyTable"

    response = dynamodb.scan(TableName=table_name)
    num_records = 15

    for i in range(num_records):
        userid = str(i)
        username = "".join(
            random.choice(string.ascii_letters) for _ in range(8)
        )  # 随机生成8个字母作为Username
        age = random.randint(18, 60)

        # 插入数据到DynamoDB表
        put_item(userid, username, age)

    for item in scan_items().items():
        print(item)
        print()


def complexQuery():
    # query the average age of those aged 30 or older
    rg =  'us-east-2' 
    dynamodb = boto3.client("dynamodb",region_name=rg)

    table_name = "MyTable"

    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression="#age > :age",
        ExpressionAttributeNames={"#age": "Age"},
        ExpressionAttributeValues={":age": {"N": "30"}},
    )

    # count total number of people and total age
    total_age = 0
    user_count = 0

    for item in response["Items"]:
        age = int(item["Age"]["N"])
        total_age += age
        user_count += 1

    # get the average age

    if user_count > 0:
        average_age = total_age / user_count
        assert average_age == 44.5
        print()
        print(f"Average Age of Users aged > 30: {average_age:.2f}")
        print()
    else:
        print("No users aged > 30 found.")

