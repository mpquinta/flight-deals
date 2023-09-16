import os
from twilio.rest import Client

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = "ACa2638faacf0f43ca9b0bddc720ad534e"
auth_token = "cf24ed4a816c27329c31a08887c75868"
client = Client(account_sid, auth_token)

class NotificationManager:
    def __init__(self):
        pass

    #This class is responsible for sending notifications with the deal flight details.
    def send_text(self, price, from_city, from_iata, to_city, to_iata, start_date, end_date):
        message = client.messages \
                    .create(
                        body=f"Low price alert! Only {price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata} from {start_date} to {end_date}.",
                        from_='+18664412539',
                        to='+14158454243'
                    )

        print(message.sid)