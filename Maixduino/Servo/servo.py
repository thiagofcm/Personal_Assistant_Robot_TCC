from  machine  import  Timer , PWM
from board import board_info
from fpioa_manager import fm
import  time

#PWM is configured through the timer and connected to the IO14 pin (Pin8 Maixduino Board)
tim  =  Timer ( Timer . TIMER0 , Timer . CHANNEL0 , mode = Timer . MODE_PWM )
S1 = PWM(tim, freq=50, duty=0, pin=14)

def  Servo ( servo , angle ):
    S1.duty(((angle*9.45)/180)+2.95)

while True:
    #180 degrees
    Servo ( S1 , 180 )
    time.sleep(1)
    #135 degree
    Servo ( S1 , 135 )
    time.sleep(1)
    #90 degrees
    Servo ( S1 , 90 )
    time.sleep(1)
    #45 degree
    Servo ( S1 , 45 )
    time.sleep(1)
    #0 degree
    Servo ( S1 , 0 )
    time.sleep(1)
