import cv2
class CameraChecker():
    def list_ports(self):
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        arr.pop(-1)
        return arr


