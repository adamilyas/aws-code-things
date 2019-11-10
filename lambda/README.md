# Loading Data to Dynamo DB using Lambda Function

Format of `s3_object`

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

Format of `s3_object['Body'].read()`
```
{
	'Records': 
		[
			{
				'eventVersion': '2.1', 
				'eventSource': 'aws:s3', 
				'awsRegion': 'ap-southeast-2', 
				'eventTime': '2019-11-07T11:47:05.284Z', 
				'eventName': 'ObjectCreated:Put', 
				'userIdentity': {'principalId': 'AWS:principal:id'}, 
				'requestParameters': {'sourceIPAddress': 'source.ip.address'}, 
				'responseElements': {
					'x-amz-request-id': 'request-id', 
					'x-amz-id-2': 'x-amz0id2'
					},
				's3': {
					's3SchemaVersion': '1.0', 'configurationId': 'configuration-id', 
					'bucket': {
						'name': 'unms-dynamodb-dataload', 'ownerIdentity': {'principalId': 'principalId'}, 
						'arn': 'arn:aws:s3:::unms-dynamodb-dataload'
						}, 
					'object': {
						'key': 'sample.json', 
						'size': 1586, 
						'eTag': 'etag', 
						'sequencer': 'sequencer'
						}
				}
		}
	]
}
```
