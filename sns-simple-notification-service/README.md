# s3 bucket is a storage resource
Can be use to store files. Movement of files in s3 bucket can be used to trigger events, for example as a trigger for lambda functions

## Create function on localstack using python (boto3)

Please check `s3-init.ipynb` for more information

we will be using `s3_resource = boto3.resource("s3")` as our resource object to
- list buckets using `s3_resource.buckets.all()`
- create bucket using `s3_resource.Bucket("myBucket").create()` (Bucket is a class) OR
- create bucket using `s3_resource.create_bucket(Bucket="myBucket")`

### File transfer
Upload and download using:
- upload `s3_resource.Bucket("myBucket").upload_fileobj(file , "key")` where "key" is the file name in the bucket
- upload `s3_bucket.upload_file('./path/to/file_to_upload.txt', "key")`
- download `s3_bucket.download_fileobj("key", file)`

where `file` is `open('./path/to/local_file.txt' , 'wb')`