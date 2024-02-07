import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setwarnings(False)

class Led():
    def __init__(self):
        """Class Builder"""

    def green_led_on(self):
        GPIO.output(2,GPIO.HIGH)
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)

    def blue_led_on(self):
        GPIO.output(3,GPIO.HIGH)
        GPIO.output(4,GPIO.LOW)

    def red_led_on(self):
        GPIO.output(3,GPIO.LOW)
        GPIO.output(4,GPIO.HIGH)

    def red_led_off(self):
        GPIO.output(4,GPIO.LOW)
        
    def blue_led_off(self):
        GPIO.output(3,GPIO.LOW)
    
    def green_led_off(self):
        GPIO.output(2,GPIO.LOW)
    


