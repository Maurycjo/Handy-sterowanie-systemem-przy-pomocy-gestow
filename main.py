
from SystemController import  SystemController
import keyboard

controller=SystemController()

volume=float(controller.get_windowsVolume())
print(volume)

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
        volume-=3
        controller.windowsVolumeDown()
    print (volume)
    print(key)
