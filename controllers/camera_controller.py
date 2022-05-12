import cv2
from controllers.camera_checker import CameraChecker
class CameraController():
    def __init__(self):
        self.camera_list=[]
        self.camera_checker = CameraChecker()
        self.available_ports,self.working_ports,self.non_working_ports = self.camera_checker.list_ports()
        self.used_camera_number=self.working_ports[0]
        self.cap=cv2.VideoCapture(self.used_camera_number)

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
        ret, frame = self.cap.read()
        return ret,frame
    def get_all_cameras(self):
        return self.camera_list
    def set_used_camera_number(self,number):
        self.used_camera_number=number

    def get_capture(self):
        return self.cap

if __name__ == '__main__':
    ap=CameraController()
    ap.get_all_camera_from_system