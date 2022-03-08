from digitalio import DigitalInOut
from gpiozero import PWMOutputDevice, Motor
from motorsetup import motorsetup
from encoder import encoder
from PID import PID
from communication import communication
import pwmio
import board
import rotaryio
import digitalio

class Machine():

    def init(self):



    def Move():
        pwmio.PWMOut(board.GP6, duty_cycle = 2**15, frequency = 500)

    def Forward():

    in4 = DigitalInOut(board.GP7)
    in4.direction = digitalio.Direction.OUTPUT
    in4.value = True

    in5 = DigitalInOut(board.GP8)
    in5.direction = digitalio.Direction.OUTPUT
    in5.value = False


    pwm = pwmio.PWMOut(board.GP6, duty_cycle = 2**15, frequency = 500)


    while True:
        pass

    def Leftsideways():



    def Rightsideways():
