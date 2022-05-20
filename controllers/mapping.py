from controllers.chrome_controller import ChromeController
from controllers.gesture_name_mapper import NameMapper
import json
from win10toast import ToastNotifier as tn
import threading
from threading import Lock
import time
class Mapping():
    def __init__(self,func_getter,sys_controller):
        self.gesture={}
        self.end = False
        self.name_mapper=NameMapper()
        self.read_configuration_from_file()
        self.controller = sys_controller
        self.chrome = ChromeController()
        self.function_getter=func_getter
        self.mutex = Lock()
        self.toaster=tn()
        self.message = []
        self.message_mutex = Lock()
        t = threading.Thread(name='daemon',target=self.show_message)
        t.start()
    def end_thread(self):
        self.end=True
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
    def show_message(self):
        while self.end is False:
            self.message_mutex.acquire()
            if len(self.message) == 1:

                self.toaster.show_toast("Gesture detected",
                                        "Gesture name: "+self.name_mapper.get_gesture_name(self.message[0])+"\n"
                                        +"Action name: "+self.gesture.get(self.message[0]),
                           duration=2.5,icon_path=None)
                self.message.clear()
            self.message_mutex.release()
            time.sleep(0.5)
    def get_gesture(self, number:int):
        self.mutex.acquire()
        for key in self.gesture.keys():
            if key==number:
                self.mutex.release()
                return True
        self.mutex.release()
        return False

    def gesture_action(self,number):
        self.message_mutex.acquire()
        if len(self.message) == 1:
            self.message[0] = number
        else:
            self.message.append(number)
        self.message_mutex.release()

        if self.get_gesture(number)  == True:
            return self.function_getter.call_function(self.gesture.get(number))
        else:
            return False

