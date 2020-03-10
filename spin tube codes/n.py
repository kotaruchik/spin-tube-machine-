import RPi.GPIO as GPIO
import time

sensor = 40 # define the GPIO pin our sensor is attached to

GPIO.setmode(GPIO.BOARD) # set GPIO numbering system to BCM
GPIO.setup(sensor,GPIO.IN) # set our sensor pin to an input

countr= 0
rpmr=0
startr = 0
endr = 0
rpmr=0
i=0

def rpm(r):
    i=0
    global countr
    global startr
    global endr
    global rpmr
    #print("1")
    if GPIO.input(40)==0:
        countr=countr+1
        if countr==2:
            startr=time.time()
        if countr==3:
            endr=time.time()
            tot=endr-startr
            rpmr=int(60/tot)
            print(rpmr)
            countr=0
            f = open("r.txt", "w")
            f.write(str(rpmr))
            f.close()
            time.sleep(0.1)
            i=1
            return rpmr
        if(i==0):
            
            print('0')
     
            
GPIO.add_event_detect(sensor, GPIO.RISING, callback=rpm)
if(i==0):
    print('0')

while True:
    time.sleep(1)

 
