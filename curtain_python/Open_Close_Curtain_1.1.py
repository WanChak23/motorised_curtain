import RPi.GPIO as GPIO
import time
import sys

def control_motor(timer):
    runMotor(100, d)
    time.sleep(timer)
    motorStop()
    
def runMotor(spd, direction):
    GPIO.output(STBY, GPIO.HIGH);
    
    if (direction == 0):
        in1 = GPIO.HIGH
        in2 = GPIO.LOW
        
    elif (direction == 1):
        in2 = GPIO.HIGH
        in1 = GPIO.LOW
        
    GPIO.output(A1, in1)
    GPIO.output(A2, in2)
    P.ChangeDutyCycle(spd)
       
def motorStop():
    GPIO.output(STBY,GPIO.LOW)
    P.start(0)
    runMotor(0, 0)
    
    
    
    
###################################################################################################    
    
    
    



GPIO.setwarnings(False)

in_put = sys.argv[1]


Freq = 100
pwma = 12
A1 = 16
A2 = 18
STBY = 22

timer = 0
 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwma,GPIO.OUT)
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(STBY,GPIO.OUT)



P = GPIO.PWM(pwma,Freq)



with open("/home/pi/curtain_python/state.txt", 'r') as S:
    S_con = S.read()

if (in_put == "CloseTheCurtain"):

    if (S_con == "opened"):   
    
        d = 0
        timer = 5
        
        P.start(100)
        control_motor(timer)
        with open("/home/pi/curtain_python/state.txt", 'w') as S:
            S.write("closed")
            
elif (in_put == "OpenTheCurtain"):
    
    if (S_con == "closed"):
        
        d = 1
        timer = 3.5
        
        P.start(100)
        control_motor(timer)
        with open("/home/pi/curtain_python/state.txt", 'w') as S:
            S.write("opened")
            
            
motorStop()
            
            
            
            
            
            
           
            
            
            
            
            
            
