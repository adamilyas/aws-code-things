import json
import boto3
import csv

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = ""
def lambda_handler(event, context):
    
    table = dynamodb.Table('table_name')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    s3_object = s3_client.get_object(Bucket=bucket,Key=file_name)
    
    file_type = file_name.split(".")[-1] # split by . and get last element
    
    record_list = []
    if file_type == "json":
		json_string = s3_object['Body'].read()
		record_list = json.loads(json_string)
    elif file_type == "csv":
        csv_string = s3_object['Body'].read().decode("utf-8")
		record_list = csv_string.split("\r\n")
		first_row_flag = True
		csv_reader = csv.reader(record_list, delimiter=',', quotechar='"')
		for row in csv_reader:
			# first, ensure that row matches
			if first_row_flag:
				if not valid_header(row):
					break
				header = row
				first_row_flag = False
			# last row
			elif len(row)==0:
				break
			else:
				record = build_record(header, row)
				record_list.append(record)		
		
    else:
        return {'statusCode': 400, 'body': json.dumps('Loading data failed')}
    
    with table.batch_writer() as batch:
        for record in record_list:
            batch.put_item(Item=record)
    
    return {'statusCode': 200,'body': json.dumps('Loading json data from Lambda!')}

def valid_header(row):
	# check valid header
	return True
	
def build_record(header, row):
	record = {}
	for i, value in enumerate(row):
		record[header[i]] = value
	return record
