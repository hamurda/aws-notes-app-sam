import uuid
from math import floor
from datetime import datetime


def get_headers():
    return {
            # "Access-Control-Allow-Headers": 'app_user_id',
            # "Access-Control-Allow-Methods": 'POST, GET, PATCH, DELETE',
            "Access-Control-Allow-Origin" : "*"
           }

def get_user_id(event):
    return event['headers']['app_user_id']

def generate_note_id():
    return str(uuid.uuid4())

def get_current_time():
    return int(floor(datetime.now().timestamp()))
