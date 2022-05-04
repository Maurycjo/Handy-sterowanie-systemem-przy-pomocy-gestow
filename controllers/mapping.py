from controllers.functions_getter import FunctionsGetter
from controllers.system_controller import SystemController
from controllers.chrome_controller import ChromeController
class Mapping():
    def __init__(self):
        self.gesture={1:"switch_window" ,
                      2:"minimize_window" ,
                      3: "minimize_window",
                      4: "minimize_window",
                      5: "minimize_window",
                      6: "minimize_window",
                      7: "minimize_window",
                      8: "minimize_window",
                      9: "brightness_down",
                      10: "volume_down",
                      11: "volume_up",
                      12: "brightness_up",
                      13: "minimize_window",
                      14: "scroll_down",
                      15: "scroll_left",
                      16: "scroll_right",
                      17: "scroll_up",
                      18: "close_window",
                      19: "minimize_window",
                      20: "minimize_window",
                      21: "minimize_window",
                      22: "maximize_window",
                      23: "zoom_in",
                      24: "minimize_window",
                      25: "zoom_out"
                      }
        self.controller = SystemController()
        self.chrome = ChromeController()
        self.function_getter=FunctionsGetter(self.controller)

    def gesture_action(self,number):
        contains=False
        key2=None
        for key in self.gesture.keys():
            if key==number:
                contains=True
                key2=key
                break
        print(contains)
        if contains is True:
            return self.function_getter.call_function(self.gesture.get(key2))
        else:
            return False
