import uuid
from math import floor
from datetime import datetime


def getHeaders():
    return {
            # "Access-Control-Allow-Headers": 'app_user_id',
            # "Access-Control-Allow-Methods": 'POST, GET, PATCH, DELETE',
            "Access-Control-Allow-Origin" : "*"
           }

def getUserID(event):
    return event['headers']['app_user_id']

def generateNoteID():
    return str(uuid.uuid4())

def getCurrentTime():
    return int(floor(datetime.now().timestamp()))
