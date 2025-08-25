#Put Items in table
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

---------------------------------------------------------------------------------------------------------------------------------

#Get Items from Table

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

response = table.get_item(
    Key={
        'emp_id': '21702332'
    }
)
print(response['Item'])

---------------------------------------------------------------------------------------------------------------------------------

#Delete Items

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

response = table.delete_item(
    Key={
        'emp_id': '21702332'
    }
)
print('items deleted successfully!!')
