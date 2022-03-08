from digitalio import DigitalInOut
from Motor import Motor
from PID import PID
import pwmio
import board
import digitalio
import time
import rotaryio
import math

class Wheel():

    def init(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runMotor = Motor(pwmDrive, dirF, dirB)
        self.runPID = PID()


