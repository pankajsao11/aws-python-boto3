# file upload
import boto3

client = boto3.client('s3')
file_read = open('demo.py').read()

response = client.put_object(
    ACL = 'private',
    Body = file_read,
    Bucket = '3tier-backnd',
    Key = 'demo.py'
)
==========================================================================================================================================

#object delete

import boto3

client = boto3.client('s3')
response = client.delete_object(
    Bucket = '3tier-backnd',
    Key = 'demo.py'
)

==========================================================================================================================================

#List buckets

import boto3

client = boto3.client('s3')
response = client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])

==========================================================================================================================================

#List Objects
import boto3

client = boto3.client('s3')

response = client.list_objects(
    Bucket = 'aws-terraf0rm-state'
)

for content in response['Contents']:
    print(content['Key'])
