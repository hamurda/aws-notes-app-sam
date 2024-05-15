# GET /note

import boto3
import os
import simplejson as json
from botocore import exceptions
from .fx import getHeaders

dynamodb_client = boto3.client("dynamodb")

tableName = os.environ.get("NOTES_TABLE")
headers = getHeaders()

def getNote_handler(event, context):
    try:
        body = dynamodb_client.query(
                TableName = tableName,
                IndexName = "note_id-index",
                ExpressionAttributeValues = {
                    ':note_id': {
                        'S': event['pathParameters']['note_id'],
                    },
                },
                KeyConditionExpression = "note_id = :note_id",
                Limit = 1
            )
        
        response = {
            "statusCode": 200,
            "headers" : headers,
        }
        
        if not body["Items"]:
            response["statusCode"] = 404
            response["body"] = "Can not find the note, please check note id."
        else:
            response["body"] = json.dumps(body["Items"], use_decimal=True)

    except exceptions as e:
        return {
            "statusCode": 400,
            "headers" : headers,
            "body": f"Error Code: {e.response['Error']['Code']}\nError Message: {e.response['Error']['Message']}"
        }
    else:
        return response