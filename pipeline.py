import boto3

s3 = boto3.client('s3')

s3.create_bucket(Bucket='my-bucket')

for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])

def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)

def list_buckets():
    for bucket in s3.list_buckets()['Buckets']:
        print(bucket['Name'])

def upload_file(bucket_name, file_name):
    s3.upload_file(file_name, bucket_name, file_name)

def download_file(bucket_name, file_name):
    s3.download_file(bucket_name, file_name, file_name)