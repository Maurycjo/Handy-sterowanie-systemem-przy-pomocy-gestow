import time

from SystemController import  SystemController
import keyboard
from ChromeController import ChromeController
controller=SystemController()
chrome=ChromeController()

volume=float(controller.get_windowsVolume())


while True:
    key=0
    key=keyboard.read_key()
    if key=='1':
        controller.scrollUp()
    elif key=='2':
        controller.scrollDown()
    elif key=='3':
        controller.windowsVolumeUp()
    elif key=='4':
        controller.windowsVolumeDown()

    elif key>='5' and key <='9':
        if key=='5':
            chrome.initWindow()
        elif key=='6':
            chrome.newWindow()
        elif key=='7':
            chrome.openYt()
        elif key=='8':
            chrome.closeCurrentTab()
        elif key=='9':
            chrome.switchTab()
        time.sleep(1)
    elif key == 'a':
        controller.minimize_window()
    elif key == 'b':
            controller.maximize_window()
    elif key == 'c':
        controller.close_window()



