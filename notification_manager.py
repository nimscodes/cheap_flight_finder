from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:

    def __int__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_sms(self, text):
        message = self.client.messages.create(
            body=text,
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
        )
        print(message.sid)