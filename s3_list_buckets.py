import boto3
from pprint import pprint
client = boto3.client('s3')
response = client.list_buckets()
"""
#Response
{
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    }
}
"""
for bucket in response['Buckets']:
    print(bucket['Name'])