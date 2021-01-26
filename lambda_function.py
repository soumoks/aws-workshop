import json
import boto3
import logging
from botocore.exceptions import ClientError

#logger config
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    table_name = 'courses'
    table = dynamodb.Table(table_name)
    logger.info("Connected to DynamoDB.")

    try:
        course_id = str(event['courseid'])
    except:
        course_id = ""

    if course_id.lower() == "all":
        #return all courses
        response = table.scan()["Items"]
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps(response)
        }
    elif course_id:
        #return individal course
        try:
            response = table.get_item(Key={'courseid': course_id})
        except ClientError as e:
            logger.error(e.response['Error']['Message'])
        else:
            return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps(response['Item'])
        }
    else: 
        error_msg = "Invalid course_id passed in request"
        logger.error(error_msg)
        return {
            'statusCode': 400,
            'headers': {
                "Access-Control-Allow-Origin": "*"
            },
            'body': json.dumps(error_msg)
        }
