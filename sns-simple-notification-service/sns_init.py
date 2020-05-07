import os
import sys
import boto3
import json
import csv
from pprint import pprint
import time



# for local aws
os.environ["aws_access_key_id"] = "key"
os.environ["aws_secret_access_key"] = "key2"


##### FILE VARIABLES #####
    
REGION = 'ap-southeast-2'

# SNS (Simple Notification Service)
SNS_PORT = 4575

# SQS (To display message from SNS)
SQS_PORT = 4576

SNS_TOPIC_NAME = "test_topic"
SQS_QUEUE_NAME = "test_queue"

##### DEFINE FILE VARIABLES ABOVE ^ #####



SNS_URL = f'http://localhost:{SNS_PORT}'
SQS_URL = f'http://localhost:{SQS_PORT}'

# GLOBAL CLIENT OBJECTS

## Create SNS client
sns_client = boto3.client('sns', region_name=REGION, endpoint_url=SNS_TOPIC_NAME)

## Create SQS client
sqs_client = boto3.client('sqs', REGION, endpoint_url=SQS_URL)


# SCRIPT EXECUTE START HERE
if __name__ == "__main__":

    # SETTING UP SNS AND SQS

    resp = sns_client.create_topic(Name=SNS_TOPIC_NAME)
    sns_topic_arn = resp['TopicArn']
    print(sns_topic_arn)
    
    resp = sqs_client.create_queue( QueueName = SQS_QUEUE_NAME)
    sqs_queue_url = resp['QueueUrl']
    print("sqs_queue_url: " + sqs_queue_url)

    sqs_client.purge_queue(QueueUrl=sqs_queue_url)

    # SET UP LINK (SUBSCRIPTION) BETWEEN SNS AND SQS
    resp = sqs_client.get_queue_attributes( QueueUrl = sqs_queue_url, AttributeNames=[ 'QueueArn' ] )
    sqs_queue_arn = resp['Attributes']['QueueArn']
    print("sqs_queue_arn: " + sqs_queue_arn)

    sns_client.subscribe(
        TopicArn = sns_topic_arn,
        Protocol = "sqs",
        Endpoint = sqs_queue_arn
    )

    while True:
        resp = sqs_client.receive_message(QueueUrl=sqs_queue_url)
        if 'Messages' in resp:
            try:
                pprint(resp['Messages'])
                print()
            except:
                pass

        time.sleep(3)