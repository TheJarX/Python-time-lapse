#from goprocam import GoProCamera, constants
from util import _gopro as ugp
from util import  _server as usv
from util import  _twilio as utl
import time


#TODO: Use Tasks with Asyncio in the next version
def main():
    gopro = ugp.connect_camera()
    
    print('Tomando foto...')
    time.sleep(15)
    photo = ugp.time_lapse(gopro_instance=gopro)
    del gopro
    if photo is not False:
        ugp.send_data(photo)
    else:
        main()
    time.sleep(30)    
    main()

    
main()
    
        
    
