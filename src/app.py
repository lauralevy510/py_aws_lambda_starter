import dotenv
dotenv.load_dotenv()

import json
from os import environ

def handler(event, context):
    return json.dumps({"vars": environ.copy()})

def second_handler(second_event, context):
    return json.dumps({"vars": environ.copy()})]
def third_handler(second_event, context):
        return json.dumps({"vars": environ.copy()})
