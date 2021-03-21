from app.gopro_utils import GoProUtils
from app.twilio_utils import TwilioUtils
from app.helpers import send_data
from app.exceptions import (
    ServerConnectionFailed,
    CameraNotFound,
    UnknownEexception
)
from dotenv import load_dotenv
import datetime as dt
from os import getenv
from time import sleep as wait

load_dotenv()

# TODO: I'm thinking in a queue of failed requests in case this program couldn't connect to wifi so we can upload the pictures when it's connected again


def trySend(pic_url, gopro):
    try:
        send_data(pic_url)
        gopro.deleteLastPicture()
        return True
    except ServerConnectionFailed:
        # TODO: read the TODO above
        trySend(pic_url, gopro)


# TODO: Use Tasks with Asyncio in the next version
def main():
    twilio = TwilioUtils(getenv('TWILIO_SID'), getenv(
        'TWILIO_TOKEN'), getenv('DEFAULT_PHONE'))
    gopro = GoProUtils()
    gopro.connect()

    print('[GoPro] Waiting for connection...')
    wait(15)

    try:
        pic_url = gopro.shoot()
        trySend(pic_url, gopro)
    except CameraNotFound:
        twilio.send_alert()
    except UnknownEexception as exception_message:
        twilio.send_alert(exception_message)

    wait(getenv('SHOOT_INTERVAL'))

    current_time = dt.datetime.now().strftime('%H %M %S').split(' ')
    now = dt.time(*current_time)
    sleep_time = dt.time(getenv('SLEEP_TIME').split(' '))

    if sleep_time <= now:
        gopro.shutdown()
        exit()
    else:
        main()


main()
