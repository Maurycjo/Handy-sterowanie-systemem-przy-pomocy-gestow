import cv2
from controllers.camera_checker import CameraChecker
from threading import Thread, Lock

class CameraController():
    def __init__(self):

        self.camera_checker = CameraChecker()
        self.camera_list = self.camera_checker.list_ports()
        self.used_camera_number=self.camera_list[0]
        self.cap=cv2.VideoCapture(self.used_camera_number)
        self.mutex = Lock()
    # def get_all_camera_from_system(self):
    #     self.camera_list.clear()
    #     for i in range(100):
    #         cap = cv2.VideoCapture(i,cv2.CAP_DSHOW)
    #         if cap.isOpened():
    #             self.camera_list.append(i)
    #             cap.release()
    #     self.camera_list.pop(-1)
    #     print(self.camera_list)

    def get_used_camera_number(self):
        return self.used_camera_number
    #Klasy camera oraz mouse_steering powinny obraz z kamery pobierać przy pomocy tej funkcji
    def get_camera_image(self):
        self.mutex.acquire()
        ret, frame = self.cap.read()
        self.mutex.release()
        return ret,frame
    def get_all_cameras(self):
        return self.camera_list
    def set_used_camera_number(self,number):
        self.mutex.acquire()
        self.used_camera_number=number
        self.cap.release()
        self.cap = cv2.VideoCapture(self.used_camera_number)
        self.mutex.release()

    def get_capture(self):
        self.mutex.acquire()
        temp=self.cap
        self.mutex.release()
        return temp

if __name__ == '__main__':
    ap=CameraController()
    print(ap.camera_list)


