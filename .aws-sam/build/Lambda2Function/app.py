import json

def handler(event, context):
    for record in event['Records']:
        body = record['body']
        print("Received message:", body)
    return {"status": "processed"}
