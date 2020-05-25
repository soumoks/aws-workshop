import json
import boto3
from pprint import pprint

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table('courses')

#sample data
"""
{
        "title": "Java fundamentals",
        "desc": "Learning java",
        "courseid": "ENSF607"
}
"""

with open('input_data.json') as json_file:
    courses = json.load(json_file)
    for course in courses:
        courseid = course['courseid']
        desc = course['desc']
        title = course['title']
        
        response = table.put_item(
            Item = {
                'courseid':courseid,
                'desc':desc,
                'title':title,
            }
        )
        print("Put item succeeded")
        print(json.dumps(response, indent=4))