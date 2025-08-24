#creating AMI from instance
import boto3

source_region = 'ap-south-1'
ec2 = boto3.resource('ec2', region_name=source_region)

instances = ec2.instances.filter(InstanceIds=['i-04145ada2f225f1a4'])

imag_ids = []
for i in instances:
    img = i.create_image(Name='AMI-Boto3-' +i.id, Description='Boto3 copied AMI'+i.id)
    imag_ids.append(img.id)

print(f"Images to be copied: {imag_ids}")

#waiting for image to be available, get waiter for image_available
client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available')

waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': imag_ids
}])

#copying image to another region
destination_region = 'us-east-1'
client = boto3.client('ec2', region_name=destination_region)

for imd in imag_ids:
    client.copy_image(Name='Boto3-copy'+imd, SourceImageId=imd, SourceRegion='ap-south-1')
