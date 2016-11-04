import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cmat = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
hmat = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
cbmat = [['?','?','?'],['?','?','?'],['?','?','?']]
whitehold = 80

while(True):
    ret, frame = cap.read()
    newframe = cv2.resize(frame, (frame.shape[1]/4, frame.shape[0]/4))
    px = newframe[newframe.shape[0]/2, newframe.shape[1]/2]
    cv2.rectangle(newframe, (40, 10), (130,100), (255,255,0), 5)

    hsv = cv2.cvtColor(newframe, cv2.COLOR_BGR2HSV)
    startx = 40
    starty = 40
    interval = 15
    for i in range(0, 3):
        for j in range(0, 3):
            nowx = 55+(30*i)
            nowy = 25+(30*j)
#            nb = int(newframe[nowy][nowx][0])
#            ng = int(newframe[nowy][nowx][1])
#            nr = int(newframe[nowy][nowx][2])
            nh = int(hsv[nowy][nowx][0])
            ns = int(hsv[nowy][nowx][1])
            nv = int(hsv[nowy][nowx][2])
            if ns<whitehold: cbmat[i][j]='W'
            elif nh>=5 and nh<25: cbmat[i][j]='O'
            elif nh>=25 and nh<42: cbmat[i][j]='Y'
            elif nh>=42 and nh<70: cbmat[i][j]='G'
#elif nh>=70 and nh<85: cbmat[i][j]='W'
            elif nh>=90 and nh<105: cbmat[i][j]='B'
            elif nh>=130 and nh<180: cbmat[i][j]='R'
            else: cbmat[i][j] = '?'
#            cv2.circle(newframe, (nowx,nowy), 5, (nb-10, ng-10, nr-10), -1)
#            cmat[i][j] = (nb, ng, nr)
            hmat[i][j] = (nh, ns, nv)

#    print "rgb"
#    print cmat[1][1]
    print "hsv"
    print hmat[1][1]
    print cbmat
#    temp = np.uint8([[0,255,0]])
#    hsv = cv2.cvtColor(temp,cv2.COLOR_BGR2HSV)
#    print "hsv"
#    print hsv
#   for i in range(0, newframe.shape[1]/2):
#        for j in range(0, newframe.shape[0]/2):
#            newframe[j, i] = px
    cv2.imshow('frame', newframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
    if cv2.waitKey(2) & 0xFF == ord('s'):
        print "start"

cap.release()
cv2.destroyAllWindows()
