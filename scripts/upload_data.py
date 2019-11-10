import boto3
import json
import csv
from boto3.dynamodb.conditions import Key, Attr
"""
To run locally:
$ java -Djava.library.path=~/dynamodb_local_latest/DynamoDBLocal_lib -jar ~/dynamodb_local_latest/DynamoDBLocal.jar -sharedDb -port 8000 -inMemory

Make sure that the columns in sample.csv contains the  AttributeNames in attribute_mapping
"""

# change these:
fn = "./sample.csv" 
REGION = 'ap-southeast-2'
URL = "http://localhost:8000"
HASH_KEY = "id"
RANGE_KEY = "sortId"
TABLE_NAME = "some_table_name"

dynamodb = boto3.resource(
    'dynamodb', 
    region_name=REGION, 
    endpoint_url=URL )

attribute_mapping = {
    "HASH": {"AttributeName": HASH_KEY, "AttributeType": "S"},
    "RANGE": {"AttributeName": RANGE_KEY, "AttributeType": "S"}
}

def create_table(TABLE_NAME, hash_key, range_key):
    dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema= [       
            { 'AttributeName': hash_key, 'KeyType': "HASH"},    # Partition key
            { 'AttributeName': range_key, 'KeyType': "RANGE" }   # Sort key
        ],
        AttributeDefinitions=[
            {'AttributeName': hash_key, 'AttributeType': 'S'},
            {'AttributeName': range_key, 'AttributeType': 'S'},
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 10,'WriteCapacityUnits': 10}
    )
    return dynamodb.Table(TABLE_NAME)

def build_record(header, row):
    record = {}
    for i, value in enumerate(row):
        col_name = header[i]
        record[col_name] = str(value)
    return record

def valid_header(header, attribute_mapping):
    for key in attribute_mapping:
        if attribute_mapping[key]["AttributeName"] not in header:
            return False
    return True

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name=REGION, endpoint_url=URL)
    table = dynamodb.Table(TABLE_NAME)
    if table not in dynamodb.tables.all():
        table = create_table(TABLE_NAME, HASH_KEY, RANGE_KEY)

    ids = set()
    csv_file = open(fn, "r")
    with table.batch_writer() as batch:
        header = []
        first_row_flag = True
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if first_row_flag:
                if not valid_header(row, attribute_mapping):
                    print(f'{row} does not match {attribute_mapping.keys()}')
                    break
                header = row
                first_row_flag = False
                continue
            record = build_record(header, row)
            record_id = record[HASH_KEY]
            ids.add(record_id)
            print(f'Adding Record({HASH_KEY}={record_id})')
            batch.put_item(Item=record)

    for id in ids:
        response = table.query(KeyConditionExpression=Key(HASH_KEY).eq(id))
        print(response)
