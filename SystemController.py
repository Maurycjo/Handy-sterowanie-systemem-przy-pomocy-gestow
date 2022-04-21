

import pyautogui

class SystemController(object):

    _scrollSpeed=200

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


