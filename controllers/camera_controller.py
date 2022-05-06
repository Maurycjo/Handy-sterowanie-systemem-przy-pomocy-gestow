import cv2
class ApplicationController():
    def __init__(self):
        self.camera_list=[]
        self.camera_list=self.get_all_camera_from_system()
        self.used_camera_number=0
        self.cap=cv2.VideoCapture(self.used_camera_number)

    def get_all_camera_from_system(self):
        self.camera_list.clear()
        for i in range(100):
            cap = cv2.VideoCapture(i,cv2.CAP_DSHOW)
            if cap.isOpened():
                self.camera_list.append(i)
                cap.release()
        self.camera_list.pop(-1)
        print(self.camera_list)

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

if __name__ == '__main__':
    ap=ApplicationController()
    ap.get_all_camera_from_system