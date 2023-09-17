import os
from twilio.rest import Client

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = "ACa2638faacf0f43ca9b0bddc720ad534e"
auth_token = "9d8dacb1d45befce6e7ce4c3183f3c2c"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)        

    #This class is responsible for sending notifications with the deal flight details.
    def send_text(self, message):
        message = self.client.messages.create(
                        body=message,
                        from_='+18664412539',
                        to='+14158454243'
                    )

        print(message.sid)