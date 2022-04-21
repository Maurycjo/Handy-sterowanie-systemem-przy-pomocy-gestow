
import platform
import pyautogui
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
except ImportError:
    pass
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class SystemController(object):

#scroll
    _scrollSpeed=200

#windows volume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volumeChange=0.6525


    def __init__(self):
        self.operating_system_name=platform.system()
        self.currentVolume=self.volume.GetMasterVolumeLevel()


    @property
    def scrollSpeed(self):
        return self._scrollSpeed
    @scrollSpeed.setter
    def scrollSpeed(self, speed):
        self._scrollSpeed=speed

    def scrollUp(self, speed=_scrollSpeed):
        pyautogui.scroll(self.scrollSpeed)

    def scrollDown(self, speed=_scrollSpeed):
        pyautogui.scroll(-self.scrollSpeed)



    def windowsVolumeUp(self):
        value=self.get_windowsVolume()+self.volumeChange
        if value>0:
            value=0
        self.currentVolume=value
        self.volume.SetMasterVolumeLevel(self.currentVolume, None)

    def windowsVolumeDown(self):
        value=self.get_windowsVolume()-self.volumeChange
        if value<-65.25:
            value=-65.25
        self.currentVolume=value
        self.volume.SetMasterVolumeLevel(self.currentVolume, None)


    def get_windowsVolume(self):
        return self.currentVolume


    def set_linux_volume(v_value: float):
        print("Place to function, which we have ")

