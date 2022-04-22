#!/usr/bin/env python
# coding: utf-8

# In[1]:

                                            #opencv koniecznie w wersji 3.4.2.16- na innych nie działa
import cv2


# In[2]:


from models import ModelType,ModelFactory
# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# In[3]:


model =ModelFactory(rgbpath='trained_models/rgblstm.h5',trained=True).getModel(ModelType.RGB)


# In[4]:


model.summary()


# In[5]:


from keras.layers import Input
from keras.models import Model


# # In[6]:
#
#
rgbinput = Input((150,100,3))

x = model.layers[1].layer(rgbinput)
for layer in model.layers[2:-3]:
    x = layer.layer(x)
x
#
#
# # In[7]:
#
#
encoder = Model(inputs = rgbinput , outputs =x)
encoder.summary()
#
#
# # In[8]:
#
#
lstminput = Input((10,1024))
#
x = model.layers[-2](lstminput)
x = model.layers[-1](x)
x
#
#
# # In[9]:
#
#
lstm = Model(inputs = lstminput , outputs =x)
lstm.summary()
#
#
# # In[10]:
#
#
import pandas as pd
valid = pd.read_csv('20bnjester_csv_files/valid.csv')
#
#
# # In[ ]:


from collections import deque
import numpy as np
import time
q = deque([np.zeros(1024) for i in range(10)] )#queue of extracted features , initialy filled with zeros
def grab_frame(cap):
   ret,frame = cap.read()
   return frame


import matplotlib.animation as animation
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
import keyboard
from matplotlib.animation import FuncAnimation

gs = gridspec.GridSpec(2, 3)  #2 rows  3 cols

fig = pl.figure()

ax1 = pl.subplot(gs[0, 1])  #ustawienie położenia zdjęcia(drugi argument-0 z lewej, 2 z prawej)
ax2 = pl.subplot(gs[1, :])  #ustawienie położenia wykresu na ekranie
#zmienna związana z wykresem


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
graph,= ax2.plot(valid.columns.values[1:] ,np.arange(27))   #wpisanie nazw etykiet oraz wartości od 0 do 26- następne wartosci na wykresie

#im1 = ax1.imshow(grab_frame(cap))

ax2.set_ylim(-1, 1)  #ustawienie zakresu osi pionowej na wykresie wartośc 0,1
#def animate(i):

while True:
    ret,frame = cap.read()
    cv2.imshow('Obraz',frame)
    im1=ax1.imshow(frame)
    im1.set_data(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))     #ustawienie kolorów zdjęcia na rgb
    q.popleft()
    plt.setp(ax2.get_xticklabels(), rotation=20, horizontalalignment='right')  #ustawienie rotacji etykiety wykresu
    q.append(encoder.predict(np.array([cv2.resize(frame/255.,(100,150))]))[0])
    our_values=lstm.predict(np.array([q]))
    graph.set_data(valid.columns.values[1:],our_values[0])     #wpisanie danych testowych do grafu
    #print(our_values)          #Szukane wartości
    if our_values[0][0]>0.9:
        print("gest0")
    if our_values[0][1]>0.9:
        print("gest1")
    if our_values[0][2]>0.9:
        print("gest2")
    if our_values[0][3]>0.9:
        print("gest3")
    if our_values[0][4]>0.9:
        print("gest4")
    if our_values[0][5]>0.9:
        print("gest5")
    if our_values[0][6]>0.9:
        print("gest6")
    if our_values[0][7]>0.9:
        print("gest7")
    if our_values[0][8]>0.9:
        print("gest8")
    if our_values[0][9]>0.9:
        print("gest9")
    if our_values[0][10]>0.9:
        print("gest10")
    if our_values[0][11]>0.9:
        print("gest11")
    if our_values[0][12]>0.9:
        print("gest12")
    if our_values[0][13]>0.9:
        print("gest13")
    if our_values[0][14]>0.9:
        print("gest14")
    if our_values[0][15]>0.9:
        print("gest15")
    if our_values[0][16]>0.9:
        print("gest16")
    if our_values[0][17]>0.9:
        print("gest17")
    if our_values[0][18]>0.9:
        print("gest18")
    if our_values[0][19]>0.9:
        print("gest19")
    if our_values[0][20]>0.9:
        print("gest20")
    if our_values[0][21]>0.9:
        print("gest21")
    if our_values[0][22]>0.9:
        print("gest22")
    if our_values[0][23]>0.9:
        print("gest23")
    if our_values[0][24]>0.9:
        print("gest24")
    if our_values[0][25]>0.9:
        print("gest25")
    if our_values[0][26]>0.9:
        print("gest26")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #return im1,#graph, zakomentowałem



    #time.sleep(0.05)

#ani = animation.FuncAnimation(fig,animate,blit=True,repeat=True,interval=5)

cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

