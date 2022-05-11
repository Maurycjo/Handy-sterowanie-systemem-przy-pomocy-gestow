import sys
sys.path.insert(0, "..")
from gesture_liblary.camera import Camera
class Controller():
    def __init__(self):
        self.camera=Camera()
    def start_gesture_recognition(self):
        self.camera.start_windows_gesture_library()
    def stop_gesture_recognition(self):
        self.camera.stop_gesture_recognition()