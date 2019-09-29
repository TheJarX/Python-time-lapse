""" 
Use this document to declare the required constants. 

! Important: Rename this file to "_constants.py" (remove "_template")

"""

#This is the MAC address of your GoPro, will not be unique for all GoPro models
DEFAULT_MAC = ''

# WLAN network data
WIFI_SSID = ''
WIFI_PASS = ''

#GoPro network data
GOPRO_WIFI = ''
GOPRO_PASS = ''

SERVER_URL = ''

#TWILIO
SID_TWILIO = ''
TOKE_TWILIO = ''
DEFAULT_TELF = ''

#TIME

import datetime as dtsu
from datetime import datetime as dt 

NOW = dt.now().strftime('%Y-%m-%d %H:%M:%S')
NOW = NOW.split(' ')
NOW = NOW[1]
NOW = ' '.join(NOW.split(':')).split(' ')
NOW  = dtsu.time(int(NOW[0]),int(NOW[1]),int(NOW[2]) )
SLEEP_TIME = dtsu.time(16,40,0)




