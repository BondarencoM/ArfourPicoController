from digitalio import DigitalInOut
from gpiozero import PWMOutputDevice, Motor
import pwmio
import board
import rotaryio
import digitalio

class Wheels():

    def init(self):
        self.motor1 = ()
        self.motor2 = ()
        self.motor3 = ()
        self.motor4 = ()

