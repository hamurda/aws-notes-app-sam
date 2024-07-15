# PATCH /note

import boto3
import os
import json
from botocore import exceptions
from .fx import get_user_id, get_headers, get_current_time


dynamodb_client = boto3.client("dynamodb")
tableName = os.environ.get("NOTES_TABLE")
headers = get_headers()


def update_note_handler(event, context):
    try:
        upd_note = json.loads(event["body"])["Item"]
    
        upd_response = dynamodb_client.update_item(
            TableName = tableName,
            Key = {
                "user_id": {"S": upd_note["user_id"]},
                "timestamp": {"N": upd_note["timestamp"]}
            },
            ExpressionAttributeValues = {
                ':uid': {"S": str(get_user_id(event))},
                ':new_note' : {"S": upd_note["note"]},
                ':nid' : {"S": upd_note["note_id"]},
            },
            UpdateExpression = "SET note = :new_note",
            ConditionExpression = "user_id = :uid AND note_id = :nid",
            ReturnValues = 'UPDATED_NEW'
        )

        response = {
            "statusCode": 200,
            "headers" : headers,
            "body": json.dumps(upd_response["Attributes"])
        }
    except exceptions.ClientError as e:
        return {
            "statusCode": 400,
            "headers" : headers,
            "body": f"Error Code: {e.response['Error']['Code']}\nError Message: {e.response['Error']['Message']}"
        }
    else:
        return response



