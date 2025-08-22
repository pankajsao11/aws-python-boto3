#Creating EBS Snapshot and notifying using SNS Topic
# Ref>> {https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/create_snapshot.html}, {https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#resources}, {https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/client/publish.html}
import boto3

ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

backup_filter = [
    {
        'Name': 'tag:Env',
        'Values': ['Dev']
    }
]

snapshot_ids = []
for r in ec2.instances.filter(Filters=backup_filter):
    for vol in r.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn = 'arn:aws:sns:ap-south-1:211125590785:bubu-baby',
    Subject = 'EBS Backup created',
    Message = str(snapshot_ids)
)
