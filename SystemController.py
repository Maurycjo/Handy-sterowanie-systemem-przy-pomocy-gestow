
import platform
import pyautogui
import ctypes

try:
    #import win32gui
    #import win32con
    from ctypes import cast, POINTER,wintypes as w
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
    def minimize_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        SW_MINIMIZE = 6
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MINIMIZE)

    def maximize_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        SW_MAXIMIZE = 3
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)
    def close_window(self):
        user32 = ctypes.WinDLL('user32')
        user32.GetForegroundWindow.argtypes = ()
        user32.GetForegroundWindow.restype = w.HWND
        user32.ShowWindow.argtypes = w.HWND, w.BOOL
        user32.ShowWindow.restype = w.BOOL
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd,0)
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
    def zoom_in(self):
        pyautogui.keyDown('ctrl')
        pyautogui.press('+')
        pyautogui.keyUp('ctrl')
    def zoom_out(self):
        pyautogui.keyDown('ctrl')
        pyautogui.press('-')
        pyautogui.keyUp('ctrl')
        
    def brightness_up(self):
        pyautogui.keyDown('fn')
        pyautogui.press('up')
        pyautogui.keyUp('fn')
    
    def brightness_down(self):
        pyautogui.keyDown('fn')
        pyautogui.press('down')
        pyautogui.keyUp('fn')

    def get_windowsVolume(self):
        return self.currentVolume


    def set_linux_volume(v_value: float):
        print("Place to function, which we have ")

