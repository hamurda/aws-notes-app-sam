# POST/note

import boto3
import os
import json
from botocore import exceptions
from .fx import generateNoteID, getCurrentTime,getUserID, getHeaders


lambda_client = boto3.client("lambda")
dynamodb_client = boto3.client("dynamodb")

tableName = os.environ.get("NOTES_TABLE")
headers = getHeaders()


def addNote_handler(event, context):
    try:
        note_content = json.loads(event["body"])["Item"]["note"]

        note_client = {
            "user_id": { "S" : getUserID(event)},
            "timestamp": { "N" : str(getCurrentTime())},
            "note_id": { "S" : generateNoteID()},
            "note": { "S" : note_content},
        }
    
        dynamodb_client.put_item(
            TableName = tableName,
            Item = note_client,
        )

        response = {
            "statusCode": 200,
            "headers" : headers,
            "body": json.dumps(note_client)
        }
    except exceptions.ClientError as e:
        return {
            "statusCode": 400,
            "headers" : headers,
            "body": f"Error Code: {e.response['Error']['Code']}\nError Message: {e.response['Error']['Message']}"
        }
    else:
        return response
