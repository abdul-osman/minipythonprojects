#install using pip3 install twilio
from twilio.rest import Client

account_sid = '' # enter account sid found on twilio account console
auth_token = ''  # enter account token found on twilio account console
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='', # create temp phone number from twilio account console
                     to=''  # enter destination number
                 )

print(message.sid)