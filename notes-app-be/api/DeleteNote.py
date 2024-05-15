# DELETE /note

import boto3
import os
import json
from botocore import exceptions
from .fx import getHeaders


dynamodb_client = boto3.client("dynamodb")
tableName = os.environ.get("NOTES_TABLE")
headers = getHeaders()


def deleteNote_handler(event, context):
    try:
        org_note = json.loads(event["body"])["Item"]
    
        delete_response = dynamodb_client.delete_item(
            TableName = tableName,
            Key = {
                "user_id": {"S": org_note["user_id"]},
                "timestamp": {"N": org_note["timestamp"]}
            },
            ReturnValues = 'ALL_OLD'
        )

        response = {
            "statusCode": 200,
            "headers" : headers,
            "body": json.dumps(delete_response["Attributes"])
        }
    except exceptions.ClientError as e:
        return {
            "statusCode": 400,
            "headers" : headers,
            "body": f"Error Code: {e.response['Error']['Code']}\nError Message: {e.response['Error']['Message']}"
        }
    else:
        return response



