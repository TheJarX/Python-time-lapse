#from goprocam import GoProCamera, constants
from util import _gopro as ugp
from util import  _server as usv
from util import  _twilio as utl
from util import _constants as _
import time




def trySend(photo, gopro):
    if photo is not False:
        res  = ugp.send_data(photo)
        if res == True:
            gopro.delete("last")
            return True
        else:
            fileUrl = 'http://10.5.5.9/videos/DCIM/100GOPRO/' +\
                        gopro.getMediaInfo('file')
            trySend(photo = fileUrl, gopro = gopro)

#TODO: Use Tasks with Asyncio in the next version
def main():
    gopro = ugp.connect_camera()
    print('Esperando conexión')
    time.sleep(15)
    photo = ugp._take_photo(gopro_instance=gopro)
    status = trySend(photo)
    # * Instead of a time lapse in _take_photo(), use this time.sleep()
    time.sleep(600)
    del(gopro)
    if not _.NOW>= _.SLEEP_TIME:
        main()
    else:
        ugp.gp_powerOff(gopro)
        exit()

    
main()
    
        
    
