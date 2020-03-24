# Python with AWS

## S3

### Reading
```
BUCKET = event['Records'][0]['s3']['bucket']['name']
FILE_NAME = event['Records'][0]['s3']['object']['key']

s3_client = boto3.client('s3')
s3_object = s3_client.get_object(Bucket=BUCKET,Key=FILE_NAME)
csv_file = s3_object["Body"]
```

### Writing (for Pandas)
```
def save_csv_to_s3(df, s3_client, bucket_name, input_file_name):
    """
    df: Pandas.DataFrame
    s3_client: boto3.client('s3')
    bucket_name: String
    input_file_name: String
    """
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    
    output_file_name = input_file_name.replace('input', 'output').replace('.csv', '-dynamo-load.csv')
    
    s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=f'{output_file_name}')
    print('Finished (save_csv_to_s3)')
```
