
#from goprocam import GoProCamera, constants
from util import _gopro as ugp
from util import  _server as usv
from util import  _twilio as utl
from util import _constants as _
import datetime
import time

now = datetime.datetime.now()
now_time = now.time()

def trySend(photo, gopro):
    if photo is not False:
        res  = ugp.send_data(photo)
        if res == True:
            gopro.delete("last")
            print("Eliminando...")
            time.sleep(15)
            return True
        else:
            fileUrl = 'http://10.5.5.9/videos/DCIM/100GOPRO/' +\
                        gopro.getMediaInfo('file')
            trySend(photo = fileUrl, gopro = gopro)

#TODO: Use Tasks with Asyncio in the next version
def main():
    if  now_time >= datetime.time(8,00) and now_time <= datetime.time(18,40):
        try:
            gopro = ugp.connect_camera()
            print('Esperando conexión')
#            utl.send_alert(message="Iniciando...")
            time.sleep(15)
            photo = ugp._take_photo(gopro_instance=gopro)
            status = trySend(photo, gopro)
    # * Instead of a time lapse in _take_photo(), use this time.sleep()
            time.sleep(10)
        #del(gopro)
#    if not _.NOW>= _.SLEEP_TIME:
            main()
#        except OSError:
 #           utl.send_alert()
#            print("OS error")
#        except socket.timeout:
 #           utl.send_alert()
        except AttributeError:
  #         utl.send_alert()
           print("Attr error")
    else:
        ugp.gp_powerOff(gopro)
   #     exit()


main()
    
            
