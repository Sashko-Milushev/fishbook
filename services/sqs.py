from datetime import datetime

import boto3


class SQSService:
    def __init__(self):
        self.url = "https://sqs.eu-central-1.amazonaws.com/263023598438/emailsending.fifo"
        self.client = boto3.client(
            "sqs",
            aws_access_key_id="AKIAT2PLNTNTIUAOB67N",
            aws_secret_access_key="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",
            region_name="eu-central-1",
        )

    def send_message(self, email):
         resp = self.client.send_message(
            QueueUrl=self.url,
            MessageBody=f'Sending mail to {email}',
            DelaySeconds=0,
            MessageAttributes={
                'Email': {
                    'DataType': 'String',
                    'StringValue': email,
                },
            },

            MessageDeduplicationId=str(datetime.utcnow().timestamp()),
            MessageGroupId=str(datetime.utcnow().timestamp()),
        )
