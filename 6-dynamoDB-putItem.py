import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

table.put_item(
    Item={
        'emp_id': '21702332',
        'Name': 'Dudu Dolewala',
        'Mobile': 3743738478
    }
)
