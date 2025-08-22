import boto3

ec2 = boto3.resource('ec2')
for r in ec2.instances.all():
    print(f"The instances details are {r.instance_id} and {r.instance_type}")


------------------------------------------------------------------------------------------------------------------------

#filtering instance details using az
import boto3

ec2 = boto3.resource('ec2')
for r in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1a']
    }
]):
    print(f"The instances details are {r.instance_id} and {r.instance_type}")

------------------------------------------------------------------------------------------------------------------------
