from wireless import Wireless
from util import _constants as _
import time

class WifiCtrl:
    
    def __init__(self, option = "WIFI"):
        self.error = False

        if option == 'WIFI' or option == 0:
            self.ssid = _.WIFI_SSID
            self.password = _.WIFI_PASS
        elif option == 'GOPRO' or option == 1:
            self.ssid = _.GOPRO_WIFI
            self.password = _.GOPRO_PASS
        else:
            self.error = True
    
    def connect(self):
        ''' Connect to a wifi network '''
        if not self.error:
            w = Wireless()
            w.interface()
            res = w.connect(ssid = self.ssid, password = self.password)
            # print(res)
            return True
        else:
            return False



