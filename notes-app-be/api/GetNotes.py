# GET /notes

import boto3
import os
import simplejson as json
from botocore import exceptions
from .fx import getHeaders, getUserID

dynamodb_client = boto3.client("dynamodb")
paginator = dynamodb_client.get_paginator('query')

tableName = os.environ.get("NOTES_TABLE")
headers = getHeaders()

def getNotes_handler(event, context):
    user_id = getUserID(event)
    response = {
                "headers" : headers,
            }
    result = []

    params = {
            'TableName' : tableName,
            'KeyConditionExpression' : "user_id = :userid",
            "ExpressionAttributeValues" : {
                ":userid" : {'S': user_id}
                    },
            "Limit" : 2,  #kept low to test pagination
            "ScanIndexForward":False, #reverse timstamp order
        }

    try:
        while True:
            body = dynamodb_client.query(**params)

            
            if not body["Items"] and not result:
                response["statusCode"] = 404
                response["body"] = "Can not find the notes, please check user id."
                return response
            else:
                result.extend(body["Items"])
            
            if "LastEvaluatedKey" in body:
                params["ExclusiveStartKey"] = {
                        "user_id" : {'S': user_id},
                        "timestamp" : body["LastEvaluatedKey"]["timestamp"],
                    }
            else:
                break
            
        response["statusCode"] = 200
        response["body"] = json.dumps(result, use_decimal=True)

    except exceptions.ClientError as e:
        return {
            "statusCode": 400,
            "headers" : headers,
            "body": f"Error Code: {e.response['Error']['Code']}\nError Message: {e.response['Error']['Message']}"
        }
    else:
        return response