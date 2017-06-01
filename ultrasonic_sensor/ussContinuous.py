import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BOARD)                     #Set GPIO pin numbering 


# BCM 26 = pin 37
# BCM 16 = pin 36
TRIG = 37
ECHO = 36


GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)  


def getDistance():
    GPIO.output(TRIG, False)                 
    print "Waiting For Sensor To Settle"
    time.sleep(1)                            

    GPIO.output(TRIG, True)                  
    time.sleep(0.00001)                      
    GPIO.output(TRIG, False)                

    while GPIO.input(ECHO)==0:               
        pulse_start = time.time()              

    while GPIO.input(ECHO)==1:               
        pulse_end = time.time()               

    pulse_duration = pulse_end - pulse_start 

    #Multiply pulse duration by 17150 to get distance and round
    # to two decimals.
    distance = pulse_duration * 17150        
    distance = round(distance, 2)            

    #Check whether the distance is within range
    if distance > 2 and distance < 400:      
        print "Distance:",distance - 0.5,"cm"
        return distance                     
    else:
        print "Out Of Range"
        return -1

