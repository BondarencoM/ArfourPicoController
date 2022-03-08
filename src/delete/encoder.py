from digitalio import DigitalInOut
import pwmio
import board
import digitalio
import time
import rotaryio
import math

class encoder():

    def init(self):
        pass

    def encoderFL():
        enc = rotaryio.IncrementalEncoder(D1, D2)
        last_position = None
        while True:
        position = enc.position
        if last_position == None or position != last_position:
            print(position)
        last_position = position

    def encoderFR():
        enc = rotaryio.IncrementalEncoder(D1, D2)
        last_position = None
        while True:
        position = enc.position
        if last_position == None or position != last_position:
            print(position)
        last_position = position



