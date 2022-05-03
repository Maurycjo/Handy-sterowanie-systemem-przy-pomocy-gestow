class FunctionsGetter:

    def __init__(self, controller):
        self.controller = controller

    def get_function(self, name):
        if name == "minimize_window":
            return self.controller.minimize_window
        elif name == "maximize_window":
            return self.controller.maximize_window
        elif name == "close_window":
            return self.controller.close_window
        elif name == "scroll_up":
            return self.controller.scroll_up
        elif name == "scroll_down":
            return self.controller.scroll_down
        elif name == "windows_volume_up":
            return self.controller.windows_volume_up
        elif name == "windows_volume_down":
            return self.controller.windows_volume_down
        elif name == "zoom_in":
            return self.controller.zoom_in
        elif name == "zoom_out":
            return self.controller.zoom_out
        elif name == "brightness_up":
            return self.controller.brightness_up
        elif name == "brightness_down":
            return self.controller.brightness_down
        elif name == "scroll_right":
            return self.controller.scroll_right
        elif name == "scroll_left":
            return self.controller.scroll_left
        elif name == "switch_window":
            return self.controller.switch_window
        else:
            return None