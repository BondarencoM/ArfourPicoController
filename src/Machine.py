from digitalio import DigitalInOut
from Wheels import Wheels
import pwmio
import board
import digitalio
import time
import rotaryio
import math
import IODefinitions as ios


class Machine():

    def init(self):
        self.front_left = Wheel(ios.FL_PWM, ios.FL_DirF, ios.FL_DirB, ios.FL_EnA, ios.FL_EnB)
        self.front_right = Wheel(ios.FR_PWM, ios.FR_DirF, ios.FR_DirB, ios.FR_EnA, ios.FR_EnB)
        self.back_left = Wheel(ios.BL_PWM, ios.BL_DirF, ios.BL_DirB, ios.BL_EnA, ios.BL_EnB)
        self.back_right = Wheel(ios.BR_PWM, ios.BR_DirF, ios.BR_DirB, ios.BR_EnA, ios.BR_EnB)

    def Forward(self):
        self.runWheels.WheelFL()
        in4 = DigitalInOut(board.GP7)
        in4.direction = digitalio.Direction.OUTPUT
        in4.value = True

        in5 = DigitalInOut(board.GP8)
        in5.direction = digitalio.Direction.OUTPUT
        in5.value = False


        pwm = pwmio.PWMOut(board.GP6, duty_cycle = 2**15, frequency = 500)


        while True:
            pass

    def Leftsideways(self):



    def Rightsideways(self):


def Main():



Main()
