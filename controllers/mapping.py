from controllers.functions_getter import FunctionsGetter
from controllers.system_controller import SystemController
from controllers.chrome_controller import ChromeController
import json
class Mapping():
    def __init__(self):
        self.gesture={}
        self.read_default_configuration_from_file()
        self.controller = SystemController()
        self.chrome = ChromeController()
        self.function_getter=FunctionsGetter(self.controller)

    def save_configuration_to_file(self):
        with open("user_configuration.json", "w") as outfile:
            json.dump(self.gesture, outfile)

    def read_configuration_from_file(self):
        with open('user_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture = {int(k): v for (k, v) in data.items()}
    def read_default_configuration_from_file(self):
        with open('default_configuration.json') as json_file:
            data = json.load(json_file)
            self.gesture.clear()
            self.gesture = {int(k): v for (k, v) in data.items()}

    def gesture_action(self,number):
        print(str(number))
        contains=False
        key2=None
        for key in self.gesture.keys():
            if key==number:
                contains=True
                key2=key
                break
        if contains is True:
            return self.function_getter.call_function(self.gesture.get(key2))
        else:
            return False
