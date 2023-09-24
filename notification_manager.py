import os
from twilio.rest import Client
import smtplib
import requests
from pprint import pprint

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

gmail = os.environ['MY_EMAIL']
gmail_pw = os.environ['EMAIL_PW']

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
    
    def send_emails(self, message):
        users_get_endpoint = "https://api.sheety.co/e8fbf885f6ddb9e986be03619cb06931/flightDeals/users"
        get_response = requests.get(url=users_get_endpoint)
        client_info = get_response.json()
        client_info_list = client_info["users"]
        # pprint(client_info)

        for client in client_info_list:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=gmail, password=gmail_pw)
                connection.sendmail(
                    from_addr=gmail, 
                    to_addrs=client["email"], 
                    msg=f"Subject:Low price alert!\n\n{message}")

# test = NotificationManager()
# test.send_emails()