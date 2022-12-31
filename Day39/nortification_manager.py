# from twilio.rest import Client
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

TWILIO_SID = "ACd7a4513ac822c8c478da38fc384312bd"
TWILIO_AUTH_TOKEN = "05aa89ab5386eed2b67226d2afb59d20"
TWILIO_VIRTUAL_NUMBER = "+19787057064"
TWILIO_VERIFIED_NUMBER = "+919599156889"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)