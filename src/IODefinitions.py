from digitalio import DigitalInOut
import pwmio
import board
import digitalio
import time
import rotaryio
import math

#Motor driving connections:

#FRONT LEFT MOTOR
#[FL (Dr1 ch1)]
#FL_PWM	-> GP2	(using PWM 1A)
FL_PWM = pwmio.PWMOut(board.GP2, duty_cycle = 0)
#FL_DirF	-> GP3	(turning forward)
FL_DirF = DigitalInOut(board.GP3)
FL_DirF.direction = digitalio.Direction.OUTPUT
#FL_DirB	-> GP4	(turning backwards)
FL_DirB = DigitalInOut(board.GP4)
FL_DirB.direction = digitalio.Direction.OUTPUT

#FRONT RIGHT MOTOR
#[FR (Dr1 ch2)]
#FR_PWM	-> GP7	(using PWM 3B)
FR_PWM = pwmio.PWMOut(board.GP7, duty_cycle = 0)

#FR_DirF	-> GP5	(turning forward)
FR_DirF = DigitalInOut(board.GP5)
FR_DirF.direction = digitalio.Direction.OUTPUT
#FR_DirB	-> GP6	(turning backwards)
FR_DirB = DigitalInOut(board.GP6)
FR_DirB.direction = digitalio.Direction.OUTPUT

#BACK LEFT MOTOR
#[BL (Dr2 ch2)]
#BL_PWM	-> GP19	(using PWM 1B)
BL_PWM = pwmio.PWMOut(board.GP19, duty_cycle = 0)
#BL_DirF	-> GP17	(turning forward)
BL_DirF = DigitalInOut(board.GP17)
BL_DirF.direction = digitalio.Direction.OUTPUT
#BL_DirB	-> GP18	(turning backwards)
BL_DirB = DigitalInOut(board.GP18)
BL_DirB.direction = digitalio.Direction.OUTPUT

#BACK RIGHT MOTOR
#[BR (Dr2 ch1)]
#BR_PWM	-> GP22	(using PWM 3A)
BR_PWM = pwmio.PWMOut(board.GP22, duty_cycle = 0)

#BR_DirF	-> GP21	(turning forward)
BR_DirF = DigitalInOut(board.GP21)
BR_DirF.direction = digitalio.Direction.OUTPUT
#BR_DirB	-> GP20	(turning backwards)
BR_DirB = DigitalInOut(board.GP20)
BR_DirB.direction = digitalio.Direction.OUTPUT

#change!
#Encoder reading connections:

#ENCODER FRONT LEFT
#FL_EnA	-> GP8
FL_EnA = DigitalInOut(board.GP8)
FL_EnA.direction = digitalio.Direction.INPUT
#FL_EnB	-> GP9
FL_EnB = DigitalInOut(board.GP9)
FL_EnB.direction = digitalio.Direction.INPUT

#ENCODER FRONT RIGHT
#FR_EnA	-> GP11
FR_EnA = DigitalInOut(board.GP11)
FR_EnA.direction = digitalio.Direction.INPUT
#FR_EnB	-> GP10
FR_EnB = DigitalInOut(board.GP10)
FR_EnB.direction = digitalio.Direction.INPUT

#ENCODER BACK LEFT
#BL_EnA	-> GP14
BL_EnA = DigitalInOut(board.GP14)
BL_EnA.direction = digitalio.Direction.INPUT
#BL_EnB	-> GP15
BL_EnB = DigitalInOut(board.GP15)
BL_EnB.direction = digitalio.Direction.INPUT

#ENCODER BACK RIGHT
#BR_EnA	-> GP13
BR_EnA = DigitalInOut(board.GP13)
BR_EnA.direction = digitalio.Direction.INPUT
#BR_EnB	-> GP12
BR_EnB = DigitalInOut(board.GP12)
BR_EnB.direction = digitalio.Direction.INPUT


