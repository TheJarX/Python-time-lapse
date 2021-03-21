from wireless import Wireless


class WifiUtils:
    """
      Convenient methods to manage a device's WiFi connection
    """

    def __init__(self, wifi_ssd, wifi_pass):
        self.wifi_ssid = wifi_ssd
        self.wifi_pass = wifi_pass

    def connect(self):
        """
          Attempts to connect to a WiFi network using the data passed to the constructor
        """
        self.connect_to(self.wifi_pass, self.wifi_pass)

    @staticmethod
    def connect_to(wifi_ssid, wifi_pass):
        """
          Attempts to connect to a WiFi network

          Args:
            wifi_ssid: (str) The Network SSID
            wifi_pass: (str) The Network password

          Returns:
            Boolean True if the connection was established
        """
        w = Wireless()
        w.interface()
        return w.connect(ssid=wifi_ssid, password=wifi_pass)
