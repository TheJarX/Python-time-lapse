from .wifi_utils import WifiUtils
from os import getenv


class TwilioUtils:
    """
    Class that provides some useful methods to send WhatsApp messages using Twilio
    """

    def __init__(self, account_sid, auth_token, receiver_phone):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.receiver_phone = receiver_phone

    def _connect_wifi(self):
        """
        Connects to a wifi network using credentials from environment variables

        Uses WifiUtils' `connect_to` method
        """
        WifiUtils.connect_to(getenv('WIFI_SSID'), getenv('WIFI_PASS'))

    def send_alert(self, message='⚠️ *Error* al conectarse con la GoPro'):
        """
        Sends and message to a mobile

        Gets both mobile numbers (sender and receiver) from the environment variables.
        """
        from twilio.rest import Client

        self._connect_wifi()

        twilio_client = Client(self.account_sid, self.auth_token)

        twilio_whatsapp_number = 'whatsapp:{}'.format(
            getenv('TWILIO_WHATSAPP_NUMBER'))
        message = twilio_client.messages.create(
            body=message,
            from_=twilio_whatsapp_number,
            to='whatsapp:{}'.format(self.receiver_phone)
        )
        print(message.sid)
