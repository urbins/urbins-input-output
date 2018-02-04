from firebase import firebase
firebase = firebase.FirebaseApplication('https://urbins-project.firebaseio.com/', None)
isReady = firebase.get('/status/flag',None)
print isReady
import RPi.GPIO as GPIO
import time

def first():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23 #pi pin 16 for recycle
    ECHO = 24 #pi pin 18 for recycle

    print "Distance Measurement In Progress"

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup (ECHO, GPIO.IN)

    GPIO.output(TRIG,False)
    print "Waiting for Sensor To Settle"
    time.sleep(1)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    

    #if (distance < 50):
    firebase.put('status','recycle',distance)

    print "Distance:", distance, "cm"

    GPIO.cleanup()
    
def second():
    GPIO.setmode(GPIO.BCM)        
    
    TRIGgar = 21 #pi 40 for garb
    ECHOgar = 20 #pi 38 for garb
    
    print "Distance Measurement In Progress"

    GPIO.setup(TRIGgar,GPIO.OUT)
    GPIO.setup (ECHOgar, GPIO.IN)

    GPIO.output(TRIGgar,False)
    print "Waiting for Sensor To Settle"
    time.sleep(1)

    GPIO.output(TRIGgar,True)
    time.sleep(0.00001)
    GPIO.output(TRIGgar,False)

    while GPIO.input(ECHOgar) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHOgar) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    

    #if (distance < 50):
    firebase.put('status','garbage',distance)

    print "Distance Garb:", distance, "cm"

    GPIO.cleanup()
    
def zeroth():
    GPIO.setmode(GPIO.BCM)        

    TRIGtop = 19 #pi 40 for garb
    ECHOtop = 26 #pi 38 for garb

    print "Distance Measurement In Progress"

    GPIO.setup(TRIGtop,GPIO.OUT)
    GPIO.setup (ECHOtop, GPIO.IN)

    GPIO.output(TRIGtop,False)
    print "Waiting for Sensor To Settle"
    time.sleep(1)

    GPIO.output(TRIGtop,True)
    time.sleep(0.00001)
    GPIO.output(TRIGtop,False)

    while GPIO.input(ECHOtop) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHOtop) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)


    if (distance < 15):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        pwm=GPIO.PWM(12, 100)
        pwm.start(15)
        #def trashsort
        time.sleep(3)
        firebase.put('status','flag',True)  
        while (firebase.get('/status/type',None)==0):
            time.sleep(1)
        if (firebase.get('/status/type',None) == 1):
            pwm.ChangeDutyCycle(10)
            time.sleep(2)
            pwm.ChangeDutyCycle(15)
        elif (firebase.get('/status/type',None) == 2):
            pwm.ChangeDutyCycle(20)
            time.sleep(2)
            pwm.ChangeDutyCycle(15)

        firebase.put('status','type',0)

    GPIO.cleanup()

while True:
    zeroth()
    first()
    second() 