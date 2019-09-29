from util import _constants as _

account_sid = _.SID_TWILIO
auth_token = _.TOKEN_TWILIO

def send_alert( message = ' ⚠️ *Error* al conectarse con la GoPro', telf = _.DEFAULT_TELF ):
	from twilio.rest import Client 
	from wireless import Wireless
	from util import _constants as _
	w= Wireless()
	w.interface()

	wf = w.connect(ssid=_.WIFI_SSID, password=_.WIFI_PASS)
	client = Client(account_sid, auth_token) 
	
	message = client.messages.create( 
								from_='whatsapp:+14155238886',  
								body= message,      
								to='whatsapp:{}'.format(telf) 
							) 
 
	print(message.sid)