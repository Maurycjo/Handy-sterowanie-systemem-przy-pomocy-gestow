# import sys
# sys.path.insert(0, "..")
from controllers.functions_getter import FunctionsGetter
from controllers.system_controller import SystemController
from controllers.chrome_controller import ChromeController
from controllers.gesture_name_mapper import NameMapper
import json
from threading import Lock
import os
class Mapping():
    def __init__(self,func_getter,sys_controller):
        self.gesture={}
        self.name_mapper=NameMapper()
        self.read_configuration_from_file()
        self.controller = sys_controller
        self.chrome = ChromeController()
        self.function_getter=func_getter
        self.mutex = Lock()
    def save_configuration_to_file(self):

        with open("user_configuration.json", "w") as outfile:
            json.dump(self.gesture, outfile)

    def read_configuration_from_file(self):

        with open('user_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture = {int(k): v for (k, v) in data.items()}
    def read_default_configuration_from_file(self):
        with open('configuration/default_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture.clear()
            self.gesture = {int(k): v for (k, v) in data.items()}
    def show_message(self,str1,str2):
        self.BalloonTip.show("Handy", str1)

    def get_gesture(self, number:int):
        self.mutex.acquire()
        for key in self.gesture.keys():
            if key==number:
                self.mutex.release()
                return True
        self.mutex.release()
        return False

    def gesture_action(self,number):
        print(str(number)+" "+self.name_mapper.get_gesture_name(number))
        # notification.notify(
        #     title='Gesture detected!',
        #     message=str(number),
        #     app_name='Handy',
        #     #app_icon='path/to/the/icon.png',
        #     timeout=1.1
        # )

        if self.get_gesture(number)  == True:
            return self.function_getter.call_function(self.gesture.get(number))
        else:
            return False

