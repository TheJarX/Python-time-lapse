from util import _constants as _
from util._twilio import Twilio
import time
import requests

class GoproUtil:
    def __init__(self):
        self.current_ms = int(round(time.time() * 1000))

    def connect_camera(self):
        """ Connect the camera, will return the object, it can be NoneType """
        from goprocam import GoProCamera, constants
        from util._wifi import WifiCtrl
        try:
            w = WifiCtrl(option='GOPRO')
            w.connect()
            time.sleep(20)
            gp = GoProCamera.GoPro(mac_address = _.DEFAULT_MAC, debug=False)
            gp.mode('0')
            gp.mode('1')
            return gp
        except OSError:
            print("Error, we're trying again...")
            self.send_alert()
            self.connect_camera()
    
    def try_send(self,photo):
        if photo is not False:
            res = self.send_data(photo)
            if res is not False:
                print("Deleting file...")
                self.delete_last_media()
                time.sleep(12)
                return 1
            else:
                gp = self.connect_camera()
                
                photo ='http://10.5.5.9/videos/DCIM/100GOPRO/'+ \
                gp.getMediaInfo('file')	
                self.try_send(photo)
        else:
            print("En efecto")
            return 0
        
    def get_as_base64(self,url):
        """
        Encode the response of a url in base64
        
        Args:
            url (str): The API URL to fetch
        
        Returns: 
            the base64 string encoded
        """

        import base64
        
        try:
            return base64.b64encode(requests.get(url).content)
        except:
            print('Connection Error!')
            return False


    def send_data(self,img):
        """  Send the image to the server """
        """
        Args:  
            img (str) : The image url, response of __gopro.take_photo()__
        Returns:
            True if the request success or False if not, or request info. 
        Raises:
        """
        from util._wifi import WifiCtrl
        import datetime

        filename = img.split('/')
        filename = str(self.current_ms) + filename[ len(filename)-1 ]
        img = self.get_as_base64(img)

        w = WifiCtrl()
        w.connect()
        time.sleep(20)
        # TODO: Usar Async/Await e investigar mas al respecto
        rq = requests.post(_.SERVER_URL + 'upload-image', \
            data = { 'b64_file' : img, 'filename' : filename, 'date': datetime.datetime.now() })
        
        
        if rq.status_code == 200 and rq.reason == 'OK':
            self.delete_last_media()
            time.sleep(12)
            return True
        else:
            self.send_alert(msg='⚠️ *ERROR* no se ha podido \
                   establecer comunicación con el servidor! ')
            print("Error: {}".format(rq))
            self.send_data(img)
        return False

    def send_alert(self, msg = False):
        tl = Twilio()
        if msg is False:
            tl.send_alert()
        else:
            tl.send_alert(msg)
    def delete_last_media(self):
        gp = self.connect_camera()
        gp.delete('last')
        