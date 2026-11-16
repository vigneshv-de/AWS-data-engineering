import boto3

s3 = boto3.client('s3')

s3.create_bucket(Bucket='my-bucket')

for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])
    