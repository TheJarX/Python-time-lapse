from wireless import Wireless
import time
class WifiCtrl:
    
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
    
    def connect(self, option = 'WIFI'):
        ''' Connect to a wifi network 
            Args: 
                option, can be 0 or 1 (WIFI and GOPRO )
        '''
        w = Wireless()
        w.interface()
        res = w.connect(ssid = self.ssid, password = self.password)
        time.sleep(15)
        print(res)




