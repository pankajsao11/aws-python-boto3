# Batch put items
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

with table.batch_writer() as batch:
    for i in range(20):
        batch.put_item(
            Item={
                'emp_id': str(i),
                'Name': f'emp-{i}',
                'Mob': f'92385744{i}'
            }
        )

#Batch delete items
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

with table.batch_writer() as batch:
    for i in range(20):
        batch.delete_item(Key={'emp_id': str(i)})
        print(f"Item: emp_id-{i} deleted successfully!!")
