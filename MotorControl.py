import wiringpi2 as wp

wp.wiringPiSetup()

for i in range(2, 6):
    wp.pinMode(i, 1)
    wp.digitalWrite(i, 0)

for i in range(21, 29):
    wp.pinMode(i, 1)
    wp.digitalWrite(i, 0)

def motor(a, b):
    print a, b
    for i in range(0, 10):
        wp.digitalWrite(a, 1)
        wp.delay(5)
        wp.digitalWrite(b, 1)
        wp.delay(5)
        wp.digitalWrite(a, 0)
        wp.delay(5)
        wp.digitalWrite(b, 0)
        wp.delay(5)

while(True):
    num = input()
    if num<10:
        if num%2==0:
            motor(num, num+1)
        else:
            motor(num, num-1)
    else:
        if num%2==1:
            motor(num, num+1)
        else:
            motor(num, num-1)
