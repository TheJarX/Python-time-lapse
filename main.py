#from goprocam import GoProCamera, constants
from util import _gopro as ugp
from util import  _server as usv
from util import  _twilio as utl
import time

while True:
    gopro = ugp.connect_camera()
    #time.sleep(20)
    if gopro:
        print('Tomando foto...')
        photo = ugp.time_lapse(gopro_instance=gopro, interval_secs = 30)
        if photo is not False:
            ugp.send_data(photo)
    else:
        print(':(')
    
#GP = GoProCamera.GoPro()
#ugp.connect_wifi('WIFI')
#time.sleep(12)
#print( ugp.send_data('https://picsum.photos/200/300') )
# print( usv.save_data( ugp.get_as_base64('https://picsum.photos/200/300')  ) )

#print( usv.save_data( ugp.get_as_base64( n_img )  ) )
