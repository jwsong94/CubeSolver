import wiringpi2 as wp
import cv2
import numpy as np
import pycuber as pc
from pycuber.solver import CFOPSolver

wp.wiringPiSetup()
cap = cv2.VideoCapture(0)

spin = [[0, 0], [1, 0], [1, 1], [0, 1]]
mpin = [21, 23, 25, 27]
state = [0, 0, 0, 0]

cbmat = [[['1','?','?'],['?','?','?'],['?','?','?']],
    [['2','?','?'],['?','?','?'],['?','?','?']],
    [['3','?','?'],['?','?','?'],['?','?','?']],
    [['?','1','?'],['?','?','?'],['?','?','?']],
    [['?','2','?'],['?','?','?'],['?','?','?']],
    [['?','3','?'],['?','?','?'],['?','?','?']]]

cbmat2 = [['?','?','?'],['?','?','?'],['?','?','?']]

whitehold = 80

cube = pc.Cube()
cubearr = ""

def GINIT():
    for i in range(2, 6):
        wp.pinMode(i, 1)
        wp.digitalWrite(i, 0)
    for i in range(21, 29):
        wp.pinMode(i, 1)
        wp.digitalWrite(i, 0)

def CCW(a, n):
    for i in range(0, n):
        state[a] = state[a]+1
        if state[a]>3: state[a]=0
        wp.digitalWrite(mpin[a], spin[state[a]][0])
        wp.digitalWrite(mpin[a]+1, spin[state[a]][1])
        wp.delay(5)

def CW(a, n):
    for i in range(0, n):
        state[a] = state[a]-1
        if state[a]<0: state[a]=3
        wp.digitalWrite(mpin[a], spin[state[a]][0])
        wp.digitalWrite(mpin[a]+1, spin[state[a]][1])
        wp.delay(5)

def CW2(a, n):
    for i in range(0, n):
        b=a+2
        state[a] = state[a]-1
        if state[a]<0: state[a]=3
        state[b] = state[b]+1
        if state[b]>3: state[b]=0
        wp.digitalWrite(mpin[a], spin[state[a]][0])
        wp.digitalWrite(mpin[a]+1, spin[state[a]][1])
        wp.digitalWrite(mpin[b], spin[state[b]][0])
        wp.digitalWrite(mpin[b]+1, spin[state[b]][1])
        wp.delay(5)

def CCW2(a, n):
    for i in range(0, n):
        b=a+2
        state[a] = state[a]+1
        if state[a]>3: state[a]=0
        state[b] = state[b]-1
        if state[b]<0: state[b]=3
        wp.digitalWrite(mpin[a], spin[state[a]][0])
        wp.digitalWrite(mpin[a]+1, spin[state[a]][1])
        wp.digitalWrite(mpin[b], spin[state[b]][0])
        wp.digitalWrite(mpin[b]+1, spin[state[b]][1])
        wp.delay(5)

def getColor(iframe, n):
    hsv = cv2.cvtColor(iframe, cv2.COLOR_BGR2HSV)
    for i in range(0, 3):
        for j in range(0, 3):
            nowx = 55+(30*i)
            nowy = 25+(30*j)
            nh = int(hsv[nowy][nowx][0])
            ns = int(hsv[nowy][nowx][1])
            nv = int(hsv[nowy][nowx][2])
            print i, j, (nh, ns, nv)
            if ns<whitehold: cbmat[n][i][j]='w'
            elif nh>=0 and nh<25: cbmat[n][i][j]='o'
            elif nh>=25 and nh<43: cbmat[n][i][j]='y'
            elif nh>=43 and nh<85: cbmat[n][i][j]='g'
            elif nh>=85 and nh<110: cbmat[n][i][j]='b'
            elif nh>=120 and nh<170: cbmat[n][i][j] = 'r'
            else: cbmat[n][i][j] = '?'
    print cbmat[n]

def makeCube():
    print cbmat
    global cubearr
    global cube
    for f in range(0, 6):
        for j in range(0, 3):
            for i in range(0, 3):
                if cbmat[f][i][j]=='r':
                    cubearr = cubearr + "0"
                elif cbmat[f][i][j]=='y':
                    cubearr = cubearr + "1"
                elif cbmat[f][i][j]=='g':
                    cubearr = cubearr + "2"
                elif cbmat[f][i][j]=='w':
                    cubearr = cubearr + "3"
                elif cbmat[f][i][j]=='o':
                    cubearr = cubearr + "4"
                elif cbmat[f][i][j]=='b':
                    cubearr = cubearr + "5"
                else:
                    cubearr = cubearr + "0"
    print(cubearr)
    print "000000000111111111222222222333333333444444444555555555"
    cube = pc.Cube(pc.array_to_cubies(cubearr))
    print(cube)
    solver = CFOPSolver(cube)
    solution = solver.solve()
    print(solution)

number = 0
face = 0
GINIT()
print cbmat[0]
while(True):
    number = number+1
    ret, frame = cap.read()
    newframe = cv2.resize(frame, (frame.shape[1]/4, frame.shape[0]/4))


#wp.delay(10)
    cv2.rectangle(newframe, (40, 10), (130, 100), (0, 0, 255), 5)
    cv2.imshow('frame', newframe)
    if cv2.waitKey(1) & 0xFF == ord('g'):
        getColor(newframe, face)
        face = face+1
    if face>5:
        makeCube()
        face=-1

cap.release()
cv2.destroyAllWindows()
