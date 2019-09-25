from util import _twilio as tl
import base64
import requests
import time
from util import _constants as _


"""
Connect with a WiFi network

Args: 
	wifi (str): WIFI or GOPRO, indicate wich wifi use.
Returns:
	Void
Raises:
	idk yet.
"""
def connect_wifi( wifi = 'WIFI' ):
	from wireless import Wireless
	
	W = Wireless()
	W.interface()
	
	if wifi == 'WIFI':
    		W.connect(ssid=_.WIFI_SSID, password=_.WIFI_PASS)
	elif wifi == 'GOPRO':
    		W.connect(ssid=_.GOPRO_WIFI, password=_.GOPRO_PASS)
	else:
			print('No option!')
			return False

"""
Connect the camera, will return the object, it can be NoneType
"""
def connect_camera():
	from goprocam import GoProCamera, constants
	connect_wifi('GOPRO')
	time.sleep(20)
	gp = GoProCamera.GoPro(mac_address=_.DEFAULT_MAC)
	
	gp.mode('0')
	gp.mode('1')
	return gp;

"""
Take a photo every N seconds, by default __600 seconds__ (10 minutes)

Args:
    interval_secs (int): Interval in seconds to take a photo
    gopro_instance (Object): Result of GoProCamera.GoPro()

Returns:
    The image URL (str)
    
Raises: 
	TypeError, Camera not defined. And send a alert. 
"""
def time_lapse(gopro_instance, interval_secs = 600):
	
	try:
		img = gopro_instance.take_photo();
		return img
	except TypeError:
		tl.send_alert()
		return False
	except:
		tl.send_alert( message = \
		'🆘*E️rror desconocido*, se requiere soporte técnico urgente!' )
		return False
	#time.sleep(interval_secs)
	#time_lapse(gopro_instance, interval_secs)
	

"""
Encode the response of a url in base64

Args:
    url (str): The API URL to fetch

Returns: 
    the base64 string encoded
    ! TODO: quitar despues
"""
def get_as_base64(url):
	return base64.b64encode(requests.get(url).content)

"""
Send the last media data from the gopro to the cloud remote server after take a photo

Args:
    gopro_instance (Object): Result of GoProCamera.GoPro() 

Returns:
    True if the request success or False if not, or request info. 

Raises:

"""
def send_data(img):
    	
	filename = img.split('/')
	filename = filename[ len(filename)-1 ]
	img = get_as_base64(img)

	connect_wifi('WIFI')
	time.sleep(20)
	# TODO: Usar Async/Await e investigar mas al respecto
	#rq = requests.post(_.SERVER_URL, data = { 'b64_file' : img, 'original_name' : filename  })
	rq = requests.post(_.SERVER_URL, data = { 'original_name' : filename  })
	
	
	if rq.status_code == 200 and rq.reason == 'OK':
		print(rq.text)
		return True
	else:
		return rq

	connect_wifi('GOPRO')

	return False





	

# print( save_data( get_as_base64('https://picsum.photos/200/300')  ) )

