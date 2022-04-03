import cv2
import mediapipe as mp
import numpy
import time
import math
#inporty do sterowania dzwiekiem systemu windowsa
#from ctypes import cast, POINTER
#from comtypes import CLSCTX_ALL
#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from subprocess import call








cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands =mpHands.Hands() #hand korzysta tylko z RGB
mpDraw=mp.solutions.drawing_utils #do rysowania kropek na rece

pTime=0
cTime=0
x1=x2=y1=y2=0
range=0
lmList=[]

#dziala tylko na windowsa
#devices= AudioUtilities.GetSpeakers()
#interface= devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#volume= cast(interface, POINTER(IAudioEndpointVolume))
#print(volume.GetVolumeRange())


#call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
currentVolume=50;



while True:
    succes, img =cap.read()
    flip_img = cv2.flip(img, 1)      #odwrocilem obraz
    imgRGB=cv2.cvtColor(flip_img, cv2.COLOR_BGR2RGB) #jak korzysta tylko z rgb to trza przekonwertowac
    #imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    #print(results) #mediapie.python.solution_base.SoultionOutputs
    #print(results.multi_hand_landmarks) #jezeli dam reke pod kamere to zwraca wartosci(detekcja reki)

    #informacje o obu rekach, handLms pojedyncza reka
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm) #wspolrzedne xyz polozenia reki
                #okreslenie wspolrzednych w pikselach
                h, w ,c=img.shape
                cx, cy= int(lm.x*w), int(lm.y*h)
                    #print(id, cx, cy) #id to numer kropki na rece
                if id==4:
                    x1, y1= cx, cy;
                if id==8:
                    x2, y2= cx, cy;
                    print("4:", x1,y1," 8: ",x2, y2,"\n")
                    cv2.line(flip_img, (x1,y1), (x2,y2), (255,255,255), 8)
                    range=math.sqrt(abs((x1-x2)^2)+abs((y1-y2)^2))
                    print("range: ", range, "\n")
                     #   cv2.circle(flip_img, (cx,cy),25,(255,0,0),cv2.FILLED)

                    if range < 10:
                        currentVolume-=5
                        call(["amixer", "-D", "pulse", "sset", "Master", str(currentVolume)+"%"])
                    elif range > 15:
                        currentVolume+=5
                        call(["amixer", "-D", "pulse", "sset", "Master", str(currentVolume)+"%"])



            mpDraw.draw_landmarks(flip_img, handLms, mpHands.HAND_CONNECTIONS)  #tu dalem image na ktorym rysuje nie musi byc imgRGB, hand_connection do polaczenia kropek

#licznik fps
    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

#fpsy konwertowane do stringa i zaokraglane
    cv2.putText(flip_img, str(int(fps)),(10, 70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image", flip_img)
    cv2.waitKey(1)