# Loading Data to Dynamo DB using Lambda Function

Format of `s3_object`
"""
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
	'ETag': '"ed5dbcb928ae00f380d6a3e2eb2730b8"', 
	'ContentType': 'text/csv', 
	'Metadata': {}, 
	'Body': <botocore.response.StreamingBody object at 0x7f0210db0a20>
}
"""

Format of `s3_object['Body'].read()`
"""
{
	'Records': 
		[
			{
				'eventVersion': '2.1', 
				'eventSource': 'aws:s3', 
				'awsRegion': 'ap-southeast-2', 
				'eventTime': '2019-11-07T11:47:05.284Z', 
				'eventName': 'ObjectCreated:Put', 
				'userIdentity': {'principalId': 'AWS:AROAVSKEZCPLJES6V76VC:d942528'}, 
				'requestParameters': {'sourceIPAddress': '203.35.135.174'}, 
				'responseElements': {
					'x-amz-request-id': 'D8AD8767D5464738', 
					'x-amz-id-2': 'x-amz0id2'
					},
				's3': {
					's3SchemaVersion': '1.0', 'configurationId': 'db05edee-0754-49b4-a1a5-805670916715', 
					'bucket': {
						'name': 'unms-dynamodb-dataload', 'ownerIdentity': {'principalId': 'A36ILPLA5ZSIM6'}, 
						'arn': 'arn:aws:s3:::unms-dynamodb-dataload'
						}, 
					'object': {
						'key': 'sample.json', 
						'size': 1586, 
						'eTag': '9559ec97960073f3981b4ec87610dc25', 
						'sequencer': '005DC404393B7518BD'
						}
				}
		}
	]
}
"""
