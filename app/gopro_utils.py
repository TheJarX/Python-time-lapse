from .twilio_utils import TwilioUtils
from .wifi_utils import WifiUtils
from .exceptions import (
    UnknownEexception,
    CameraNotFound,
)
from goprocam import GoProCamera
from os import getenv
import time
from datetime import datetime as dt


class GoProUtils:
    """
    Convenient methods to control a GoPro

    Attributes:
        mac_address: The GoPro MAC Address.
        gp_instance: The GoProCamera (from goprocam) instance. It is set after the
        method connect is called.
    """

    def __init__(self, mac_address=None):
        self.mac = mac_address
        self.gp_instance = None

    def connect(self):
        """
        Attempts to connect the camera, will return the object, it can be NoneType

        This method will obtain the GoPro credentials from environment variables.

        Uses WifiUtils' `connect_to` method.

        Returns: Void
        """
        WifiUtils.connect_to(getenv('GOPRO_WIFI'), getenv('GOPRO_PASS'))
        time.sleep(20)
        gp = GoProCamera.GoPro(mac_address=self.mac)

        gp.mode('0')
        gp.mode('1')

        self.gp_instance = gp

    def shoot(self):
        """
        Take a photo

        Returns:
            The image URL (str)

        Raises:
            CameraNotFound: Camera not defined
            UnknownError: Something went wrong
        """
        try:
            return self.gp_instance.take_photo(timer=0)
        except TypeError:
            raise CameraNotFound
        except AttributeError:
            raise CameraNotFound
        except:
            raise UnknownEexception(
                '🆘*E️rror desconocido*, se requiere soporte técnico urgente!')

    def getLasMedia(self):
        """
        Gets the URL of the last media found in the GoPro

        Returns: The image URL (str)

        Raises:
            CameraNotFound: Camera not defined
        """
        try:
            # this url seems to be constant
            return 'http://10.5.5.9/videos/DCIM/100GOPRO/' + self.gp_instance.getMediaInfo('file')
        except TypeError:
            raise CameraNotFound
        except AttributeError:
            raise CameraNotFound

    def deleteLastPicture(self):
        self.gp_instance.delete('last')

    def shutdown(self):
        """
        Shutdowns the GoPro

        Note: At the moment this method won't be available, because I'm figuring out how to turn on the camera back.
        """
        return None
        # TODO: Finish the implementation of this method
        # self.connect()
        # time.sleep(20)
        # self.gp_instance.power_off()
