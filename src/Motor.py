from digitalio import DigitalInOut
import pwmio
import board
import digitalio
import time
import rotaryio
import math

class Motor():

    def init(self, pwmDrive, dirF, dirB):
        self.PWM_drive = pwmDrive
        self.Forward = dirF
        self.Backward = dirB

    def Move(direction_wheel, speed):



