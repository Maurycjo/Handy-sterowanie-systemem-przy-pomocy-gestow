
from SystemController import  SystemController
import keyboard

controller=SystemController()


while True:
    key=0
    key=keyboard.read_key()
    if key=='=':
        controller.scrollUp()
    elif key=='-':
        controller.scrollDown()
    print(key)
