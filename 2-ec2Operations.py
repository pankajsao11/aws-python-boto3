import boto3

ec2 = boto3.client('ec2')\
#for starting instances
ec2.start_instances(InstanceIds=['i-02b3d6a0030115666', 'i-04e3a8eb0bca13045', 'i-0c565568f63b1672d']) 

-----------------------------------------------------------------------------------------------------------------------
#for stopping instances
ec2.stop_instances(InstanceIds=['i-02b3d6a0030115666', 'i-04e3a8eb0bca13045', 'i-0c565568f63b1672d']) 

------------------------------------------------------------------------------------------------------------------------
#for terminating instances:
import boto3

ec2 = boto3.client('ec2')
resp = ec2.terminate_instances(InstanceIds=['i-02b3d6a0030115666', 'i-04e3a8eb0bca13045', 'i-0c565568f63b1672d'])

for instance in resp['TerminatingInstances']:
    print(f"The instance with ids {instance['InstanceId']} is terminated")

------------------------------------------------------------------------------------------------------------------------

#Describe Instances
import boto3

ec2 = boto3.client('ec2')
resp = ec2.describe_instances()

for r in resp['Reservations']:
    for instance in r['Instances']:
        print(f"The instances are {instance['InstanceId']}")

------------------------------------------------------------------------------------------------------------------------

#filtering instances based on values

import boto3
ec2 = boto3.client('ec2')
resp = ec2.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }])

for r in resp['Reservations']:
    for instance in r['Instances']:
        print(f"The stopped instances are {instance['InstanceId']}")

------------------------------------------------------------------------------------------------------------------------
