import boto3

client = boto3.client('ec2')
resp = client.run_instances(
    ImageId='ami-084568db4383264d4',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

for instance in resp['Instances']:
    print(f'The instance launched using boto is {instance['InstanceId']}')
