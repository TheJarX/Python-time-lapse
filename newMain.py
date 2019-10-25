from util import _gopro as ugp
import datetime
import time

now = datetime.datetime.now()
now_time = now.time()


def trySend(photo, gopro):
	if photo is not False:
		res = ugp.send_data(photo)
		if res is not False:
			print("Deleting file...")
			gopro.delete(option=0)
			time.sleep(12)
			return 1
		#return 1
		else:
			photo ='http://10.5.5.9/videos/DCIM/100GOPRO/'+ \
			gopro.getMediaInfo('file')	
			trySend(photo, gopro)
	else:
		print("En efecto")
		return 0


def main():
	if  now_time >= datetime.time(8,00) and now_time <= datetime.time(18,40):
		#try:
		if True:
			gopro = ugp.connect_camera()
			photo = gopro.take_photo()
			print(photo)
			res = trySend(photo, gopro)
			print(res)			
			#if res is not False:
			#	main()
		#except:
		#	print("Some error")
	else: 
		ugp.poweroff()
		

main()