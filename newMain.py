from util import _constants as _
from util._goproclass import GoproUtil
import datetime
import time

now = datetime.datetime.now()
now_time = now.time()



def main():
	gputil = GoproUtil()
	camera = gputil.connect_camera()
	try:
		if  now_time >= datetime.time(8,00) and now_time <= datetime.time(18,40):
			photo = camera.take_photo()
			print(photo)
			gputil.send_data(photo)
			time.sleep(600)
			main()

		else: 
			pass
			main()
	except AttributeError:
			gputil.send_alert()
			main()
		

main()