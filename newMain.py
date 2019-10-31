from util import _gopro as ugp
from util import _constants as _
# * quitar esto luego
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
				# camera.power_on(_.DEFAULT_MAC)
				# time.sleep(12)
			
			# if True:
				# gopro = ugp.connect_camera()
				# photo = gopro.take_photo()
				# print(photo)
				# res = trySend(photo, gopro)
				# print(res)			
				#if res is not False:
				#	main()
			#except:
			#	print("Some error")
			print("si")
			photo = camera.take_photo()
			print(photo)
			gputil.send_data(photo)
			time.sleep(30)
			main()

		else: 
			print("no")
			# camera.power_off()
			pass;
			main()
	except AttributeError:
			main()
		#try:
		

main()