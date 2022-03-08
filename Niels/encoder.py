from digitalio import DigitalInOut
from gpiozero import PWMOutputDevice, Motor
import pwmio
import board
import rotaryio
import digitalio

class encoder():

    def init(self):


enc = rotaryio.IncrementalEncoder(D1, D2)
last_position = None
while True:
    position = enc.position
    if last_position == None or position != last_position:
        print(position)
    last_position = position
