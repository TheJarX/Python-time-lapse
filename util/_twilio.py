from twilio.rest import Client
from wireless import Wireless
from util._wifi import WifiCtrl
import time


class Twilio:
	
	def __init__(self):
		pass
	
	def send_alert(self, message = '⚠️ *Error* al conectarse con la GoPro'):
		from util import _constants as _
		alert_msg = message
		w = WifiCtrl()
		w.connect()

		time.sleep(15)
		
		client = Client(_.SID_TWILIO, _.TOKEN_TWILIO) 

		message = client.messages.create( 
									from_='whatsapp:+14155238886',  
									body= alert_msg,      
									to='whatsapp:{}'.format(_.DEFAULT_TELF) 
								) 
		print(message.sid)
