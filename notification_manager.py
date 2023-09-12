import os
from twilio.rest import Client
TWILIO_SID = 'AC546a5d8ba3eef1aff634c88891c0a71c'
twilio_auth_token = os.getenv('TWILIO_AUTHEN')
TWILIO_VIRTUAL_NUMBER = '+14012133239'
TWILIO_VERIFIED_NUMBER = '+2348163040200'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, twilio_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
