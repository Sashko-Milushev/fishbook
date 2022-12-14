import boto3


class SESService:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id="AKIAT2PLNTNTIUAOB67N",
            aws_secret_access_key="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",
            region_name='eu-central-1')

    def send_email(self, email):
        response = self.client.send_email(
            Source='pythcorewin@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to our website.',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'Welcome to Fishbook. To enjoy the full experience, please finish your profile.',
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': 'string',
                        'Charset': 'string'
                    }
                }
            },
        )
