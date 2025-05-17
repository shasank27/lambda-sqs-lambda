import boto3
import os
import json

sqs = boto3.client('sqs')
queue_url = os.environ['SQS_QUEUE_URL']
print(queue_url)

def handler(event, context):
    message = {
        "id": "abc123",
        "payload": "Message from Lambda1"
    }

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )
    print("Message sent:", response['MessageId'])
    return {"status": "sent"}
