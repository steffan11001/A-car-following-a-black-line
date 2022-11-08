import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#motor dreapta
GPIO.setup(5,GPIO.OUT)
#motor stanga
GPIO.setup(7,GPIO.OUT)

irs = GPIO.setup(11,GPIO.IN)
irm = GPIO.setup(13,GPIO.IN)
ird = GPIO.setup(15,GPIO.IN)

t=0.01

def mdgo():
    GPIO.output(5,1)
    time.sleep(t)
    GPIO.output(5,0)
def msgo():
    GPIO.output(7,1)
    time.sleep(t)
    GPIO.output(7,0)
def mdmsgo():
    GPIO.output(5,1)
    GPIO.output(7,1)
    time.sleep(t)
    GPIO.output(5,0)
    GPIO.output(7,0)
def mStop():
    GPIO.output(5,0)
    GPIO.output(7,0)
while 1:
    irsValue=GPIO.input(11)
    irmValue=GPIO.input(13)
    irdValue=GPIO.input(15)
    x=irsValue + 2* irmValue +4 * irdValue
    if(x==0):
        mStop()
    if(x==1):
        msgo()
    if(x==2):
        mdmsgo()
    if(x==3):
        mdmsgo()
    if(x==4):
        mdgo()
    if(x==5):
        mdmsgo()
    if(x==6):
        mdmsgo()
    if(x==7):
        mdmsgo()
    print(x)
