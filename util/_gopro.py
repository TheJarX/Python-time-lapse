from util import _twilio
import base64
import requests
import time
import datetime
from util import _constants as _


tl = _twilio.Twilio()

#Variables

CURRENT_MS = int(round(time.time() * 1000))
#BASE_FILENAME = 'GOPRO-{}{}.jpg'.format( dt.now().strftime('%H%M%S'), \
#   CURRENT_MS )



def connect_wifi( wifi = 'WIFI' ):

    """
        Connect WiFi network

        Args: 
            wifi (str) WIFI or GOPRO, indicate wich wifi use.

        Returns:
            Void

        Raises:
            idk yet.
    """

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


def connect_camera():

    """ Connect the camera, will return the object, it can be NoneType """

    from goprocam import GoProCamera, constants
    connect_wifi('GOPRO')
    time.sleep(20)
    gp = GoProCamera.GoPro(mac_address=_.DEFAULT_MAC)
    gp.power_on()
    gp.mode('0')
    gp.mode('1')
    return gp;

def gp_powerOff(gp):
    """ 
    power off gopro
    
    Args:
        gp (Object): GoPro isntance
    
    Returns: Void

    Raises: Idk yet
    """
    connect_wifi("GOPRO")
    time.sleep(20)
    gp.power_off()

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
def _take_photo(gopro_instance, interval_secs = 600):
    """ Take a photo, this function still in dev """
    
    try:
    	  print("taking photo...")
    	  img = gopro_instance.take_photo()
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
    


def get_as_base64(url):
    """
    Encode the response of a url in base64
    
    Args:
        url (str): The API URL to fetch
    
    Returns: 
        the base64 string encoded
    """
    
    return base64.b64encode(requests.get(url).content)

"""
Send the last media data from the gopro to the cloud remote server after take a photo

Args:
    img (str) : The image url, response of __gopro.take_photo()__
Returns:
    True if the request success or False if not, or request info. 

Raises:

"""
def send_data(img):
    """  Send the image to the server """
    filename = img.split('/')
    filename = filename[ len(filename)-1 ]
    img = get_as_base64(img)

    connect_wifi('WIFI')
    time.sleep(20)
    # TODO: Usar Async/Await e investigar mas al respecto
    rq = requests.post(_.SERVER_URL + 'upload-image', \
        data = { 'b64_file' : img, 'filename' : filename, 'date': datetime.datetime.now() })
    
    
    if rq.status_code == 200 and rq.reason == 'OK':
        # print(rq.text)
        return True
    else:
   #     tl.send_alert(message='⚠️ *ERROR* no se ha podido \
    #        establecer comunicación con el servidor! ')
    	print(rq.text)
    	print("Error: {}".format(rq))
    	return rq

    connect_wifi('GOPRO')
    time.sleep(20)
    return False





    

# print( save_data( get_as_base64('https://picsum.photos/200/300')  ) )

