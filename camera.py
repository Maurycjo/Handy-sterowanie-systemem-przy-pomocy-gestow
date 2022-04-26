#!/usr/bin/env python
# coding: utf-8

                                            #opencv koniecznie w wersji 3.4.2.16- na innych nie działa


from models import ModelType,ModelFactory
from keras.layers import Input
from keras.models import Model
import pandas as pd
from collections import deque
import numpy as np
import datetime
import cv2
from SystemController import  SystemController
from ChromeController import ChromeController
controller=SystemController()
chrome=ChromeController()

def start_windows_gesture_library():


    model = ModelFactory(rgbpath='trained_models/rgblstm.h5', trained=True).getModel(ModelType.RGB)

    model.summary()

    rgbinput = Input((150, 100, 3))

    x = model.layers[1].layer(rgbinput)
    for layer in model.layers[2:-3]:
        x = layer.layer(x)
    x

    encoder = Model(inputs=rgbinput, outputs=x)
    encoder.summary()

    lstminput = Input((10, 1024))
    #
    x = model.layers[-2](lstminput)
    x = model.layers[-1](x)
    x

    lstm = Model(inputs=lstminput, outputs=x)
    lstm.summary()

    valid = pd.read_csv('20bnjester_csv_files/valid.csv')

    q = deque([np.zeros(1024) for i in range(10)])  # queue of extracted features , initialy filled with zeros

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time_before=datetime.datetime.now()
    time_now=time_before
    gesture=False
    no_wait=False
    position=0
    max_value=0.0
    while True:
        ret, frame = cap.read()
        cv2.imshow('Obraz', frame)
        q.popleft()
        q.append(encoder.predict(np.array([cv2.resize(frame / 255., (100, 150))]))[0])
        our_values = lstm.predict(np.array([q]))
        # print(our_values)          #Szukane wartości
        time_now=datetime.datetime.now()
        c=time_now-time_before
        if float(c.total_seconds())>1.0:    #Zapobiega wykrywaniu jednego wykonanego gestu kilka razy
            no_wait=True
        else:
            no_wait=False
        if gesture==False or no_wait:
            gesture=False
            position=0
            max_value=-10.0
            for i in range(len(our_values[0])):
                if our_values[0][i]>max_value:
                    max_value=our_values[0][i]
                    position=i
            if our_values[0][0] > 0.9 and position==0:
                time_before=datetime.datetime.now()
                gesture=True
                print("gest0")
            elif our_values[0][1] >0.9 and position==1:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest1")
            elif our_values[0][2] > 0.9 and position==2:
                print("no gesture")
            elif our_values[0][3] > 0.9 and position==3:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest3")
            elif our_values[0][4] > 0.9 and position==4:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest4")
            elif our_values[0][5] > 0.9 and position==5:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest5")
            elif our_values[0][6] > 0.9 and position==6:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest6")
            elif our_values[0][7] > 0.9 and position==7:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest7")
            elif our_values[0][8] > 0.9 and position==8:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest8")
            elif our_values[0][9] > 0.9 and position==9:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest9")
            elif our_values[0][10] > 0.9 and position==10:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest10")
            elif our_values[0][11] > 0.9 and position==11:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest11")
            elif our_values[0][12] > 0.9 and position==12:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest12")
            elif our_values[0][13] > 0.9 and position==13:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest13")
            elif our_values[0][14] > 0.9 and position==14:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest14")
            elif our_values[0][15] > 0.9 and position==15:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest15")
                controller.scrollDown()
            elif our_values[0][16] > 0.9 and position==16:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest16")
            elif our_values[0][17] > 0.9 and position==17:
                time_before = datetime.datetime.now()
                controller.scrollUp()
                gesture = True
                print("gest17")
            elif our_values[0][18] > 0.90 and position==18:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest18")
                controller.scrollUp()
            elif our_values[0][19] > 0.9 and position==19:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest19")
            elif our_values[0][20] > 0.9 and position==20:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest20")
            elif our_values[0][21] > 0.9 and position==21:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest21")
            elif our_values[0][22] > 0.9 and position==22:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest22")
            elif our_values[0][23] > 0.9 and position==23:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest23")
            elif our_values[0][24] > 0.9 and position==24:
                time_before = datetime.datetime.now()
                gesture = True
                controller.zoom_in()
                print("gest24")
            elif our_values[0][25] > 0.9 and position==25:
                time_before = datetime.datetime.now()
                gesture = True
                print("gest25")
            elif our_values[0][26] > 0.9 and position==26:
                time_before = datetime.datetime.now()
                gesture = True
                controller.zoom_out()
                print("gest26")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
