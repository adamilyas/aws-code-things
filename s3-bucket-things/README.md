# S3 Bucket things

## Via awscli

```
aws s3api list-objects --bucket custom-load

aws s3api get-object --bucket custom-load --key file.csv file.csv
aws s3api get-object --bucket custom-load --key folder-name/file.csv file.csv
```
If the file is in a folder in s3 bucket, please specify the foldername

## Reading from S3 Bucket via boto3 (Python3)

### Python Code

```python
import boto3

s3_client = boto3.client('s3')
bucket = event['Records'][0]['s3']['bucket']['name']

file_name = event['Records'][0]['s3']['object']['key']
s3_object = s3_client.get_object(Bucket=bucket,Key=file_name)
```

### Format of `s3_object`

```
{
	'ResponseMetadata': {
		'RequestId': 'requestId', 
		'HostId': 'hostId', 
		'HTTPStatusCode': 200, 
		'HTTPHeaders': {
			'x-amz-id-2': 'hostId', 
			'x-amz-request-id': 'requestId', 
			'date': 'Thu, 07 Nov 2019 13:07:27 GMT', 
			'last-modified': 'Thu, 07 Nov 2019 13:07:26 GMT', 
			'etag': '"etag"', 
			'accept-ranges': 'bytes', 
			'content-type': 'text/csv', 
			'content-length': '286', 
			'server': 'AmazonS3'
			}, 
		'RetryAttempts': 0
		}, 
	'AcceptRanges': 'bytes', 
	'LastModified': datetime.datetime(2019, 11, 7, 13, 7, 26, tzinfo=tzutc()), 
	'ContentLength': 286, 
	'ETag': '"eTag"', 
	'ContentType': 'text/csv', 
	'Metadata': {}, 
	'Body': <botocore.response.StreamingBody object at 0x7f0210db0a20>
}
```
You want to be able to access `s3_object['Body']` via `s3_object['Body'].read()`