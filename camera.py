# opencv koniecznie w wersji 3.4.2.16- na innych nie działa

from keras.layers import Input
from keras.models import Model
from collections import deque
import numpy as np
import datetime
import cv2

from controllers.system_controller import SystemController
from controllers.chrome_controller import ChromeController
from gesture_liblary.models import ModelType, ModelFactory


def start_windows_gesture_library():

    controller = SystemController()
    chrome = ChromeController()

    model = ModelFactory(rgbpath='trained_models/rgblstm.h5', trained=True).getModel(ModelType.RGB)

    model.summary()

    rgbinput = Input((150, 100, 3))

    x = model.layers[1].layer(rgbinput)
    for layer in model.layers[2:-3]:
        x = layer.layer(x)

    encoder = Model(inputs=rgbinput, outputs=x)
    encoder.summary()

    lstminput = Input((10, 1024))
    #
    x = model.layers[-2](lstminput)
    x = model.layers[-1](x)

    lstm = Model(inputs=lstminput, outputs=x)
    lstm.summary()
    q = deque([np.zeros(1024) for i in range(10)])  # queue of extracted features , initialy filled with zeros

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # parametryzacja-wybór kamery w aplikacji
    time_before = datetime.datetime.now()
    time_now=time_before
    gesture=False
    no_wait=False
    position=0
    max_value=0.0
    wait_time=1.0
    while True:
        ret, frame = cap.read()
        cv2.imshow('Obraz', frame)
        q.popleft()
        q.append(encoder.predict(np.array([cv2.resize(frame / 255., (100, 150))]))[0])
        our_values = lstm.predict(np.array([q]))
        # print(our_values)          #Szukane wartości
        time_now = datetime.datetime.now()
        c = time_now-time_before
        if float(c.total_seconds()) > wait_time:    #Zapobiega wykrywaniu jednego wykonanego gestu kilka razy
            no_wait=True
        else:
            no_wait=False
        if gesture==False or no_wait:
            gesture=False
            position=0
            max_value = -10.0
            for i in range(len(our_values[0])):
                if our_values[0][i] > max_value:
                    max_value = our_values[0][i]
                    position = i
            if max_value > 0.9 and position == 0:
                time_before=datetime.datetime.now()
                print("doing something, no gesture")
            elif max_value > 0.9 and position == 1:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0     #czas oczekiwania na następny gest
                controller.switch_window()
                print("gest1")
            elif max_value > 0.9 and position == 2:
                print("no gesture")
            elif max_value > 0.9 and position == 3:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest3")
            elif max_value > 0.9 and position == 4:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest4")
            elif max_value > 0.9 and position == 5:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest5")
            elif max_value > 0.9 and position == 6:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest6")
            elif max_value > 0.9 and position == 7:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest7")
            elif max_value > 0.9 and position == 8:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest8")
            elif max_value > 0.9 and position == 9:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest9")
            elif max_value > 0.9 and position == 10:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                controller.brightness_down()
                print("gest10")
            elif max_value > 0.7 and position == 11:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest11")
                wait_time = 1.0
                controller.windows_volume_down()
            elif max_value > 0.7 and position == 12:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                controller.windows_volume_up()
                print("gest12")
            elif max_value > 0.7 and position == 13:
                time_before = datetime.datetime.now()
                gesture = True
                controller.brightness_up()
                wait_time = 1.0
                print("gest13")
            elif max_value > 0.9 and position == 14:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest14")
            elif max_value > 0.7 and position == 15:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest15")
                controller.scroll_down()
            elif max_value > 0.9 and position == 16:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest16")
                controller.scroll_left()
            elif max_value > 0.9 and position == 17:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest17")
                controller.scroll_right()
            elif max_value > 0.90 and position == 18:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest18")
                controller.scroll_up()
            elif max_value > 0.9 and position == 19:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest19")
            elif max_value > 0.9 and position == 20:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest20")
            elif max_value > 0.9 and position == 21:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest21")
            elif max_value > 0.9 and position == 22:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest22")
            elif max_value > 0.9 and position == 23:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                print("gest23")
            elif max_value > 0.9 and position == 24:
                time_before = datetime.datetime.now()
                gesture = True
                wait_time = 1.0
                controller.zoom_in()
                print("gest24")
            elif max_value > 0.9 and position == 25:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest25")
                wait_time = 1.0
            elif max_value > 0.9 and position == 26:
                time_before = datetime.datetime.now()
                gesture = True
                controller.zoom_out()
                wait_time = 1.0
                print("gest26")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    start_windows_gesture_library()