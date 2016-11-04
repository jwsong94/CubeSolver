import wiringpi2 as wp
import cv2
import numpy as np
import pycuber as pc
from pycuber.solver import CFOPSolver

wp.wiringPiSetup()
cap = cv2.VideoCapture(0)

spin = [[0, 0], [1, 0], [1, 1], [0, 1]]
mpin = [21, 23, 25, 27, 2, 4]
state = [0, 0, 0, 0, 0, 0]
#mstate = [0, 0]
#mmpin = [2, 4]

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


def MoveMotorIn(a, n):
    ddd = 15
    for i in range(0, n):
        if n%4==3 and ddd>5: ddd = ddd-1
        mstate[a] = mstate[a]-1
        if mstate[a]<0: mstate[a]=3
        wp.digitalWrite(mmpin[a], spin[mstate[a]][0])
        wp.digitalWrite(mmpin[a]+1, spin[mstate[a]][1])
        wp.delay(ddd)

def MoveMotorOut(a, n):
    ddd = 15
    for i in range(0, n):
        if n%4==3 and ddd>5: ddd =ddd-1
        mstate[a] = mstate[a]+1
        if mstate[a]>3: mstate[a]=0
        wp.digitalWrite(mmpin[a], spin[mstate[a]][0])
        wp.digitalWrite(mmpin[a]+1, spin[mstate[a]][1])
        wp.delay(5)

number = 0
GINIT()

while(True):
    wp.delay(2500)
    CW(0, 50)
    wp.delay(2500)
    CCW(0, 50)
    wp.delay(2500)
    CW(1, 50)
    wp.delay(2500)
    CCW(1, 50)
    wp.delay(2500)
    CCW(2, 50)
    wp.delay(2500)
    CW(2, 50)
    wp.delay(2500)
    CCW(3, 50)
    wp.delay(2500)
    CW(3, 50)

#    wp.delay(2500)
#    MoveMotorIn(0, 100)
#    wp.delay(2500)
#    CW(0, 50)
#    wp.delay(2500)
#    MoveMotorOut(0, 100)
#    wp.delay(2500)
#    CCW(0, 50)

#    wp.delay(2500)
#    CW2(0, 50)
#    wp.delay(2500)
#    CCW2(0, 50)
#    wp.delay(2500)
#    CW2(1, 50)
#    wp.delay(2500)
#    CCW2(1, 50)


