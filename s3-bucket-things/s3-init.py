import os
import boto3

# for local aws
# os.environ["aws_access_key_id"] = "key"
# os.environ["aws_secret_access_key"] = "key2"

REGION = 'ap-southeast-2'
URL = "http://localhost:4572"
bucket_name = "myBucket"

s3_resource = boto3.resource(
    's3', 
    region_name=REGION, 
    endpoint_url=URL )

s3_bucket = s3_resource.Bucket(bucket_name)
if s3_bucket not in s3_resource.buckets.all():
    s3_bucket.create()

for obj in s3_bucket.objects.all():
    print(obj)