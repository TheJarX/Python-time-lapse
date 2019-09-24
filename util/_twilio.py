account_sid = 'AC6d97b5aba62d91b7eb038bd18aaf5a93' 
auth_token = '9549a83cb99bb61f9c634affb29cd4fb' 

def send_alert( message = ' ⚠️ *Error* al conectarse con la GoPro', telf = '+51951270619' ):
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