import sys
sys.path.insert(0, "..")
from gesture_liblary.camera import Camera
import threading
class Controller():
    def __init__(self):
        self.camera = Camera()
        self.started = False
    def start_gesture_recognition(self):
        if self.started is False:
            self.started = True
            self.t=threading.Thread(name='daemon',target=self.camera.start_windows_gesture_library)
            self.t.start()

    def stop_gesture_recognition(self):
        self.camera.stop_gesture_recognition()
        self.t.join()
        self.started=False