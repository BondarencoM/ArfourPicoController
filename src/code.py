# The imports of all used libraries
import time
import protocol

## Setup
comms = protocol.Protocol()

current_command = [None]

## Loop
while True:
    current_command = comms.update_command()
    print("in loop: ", current_command)

    time.sleep(2)
from Machine import Machine
import time
from Wheel import Wheel
print("Starting")
m = Machine()

#m.Move(0, 465, 50)
#m.Move(0, 465, 50)

while True:
    speed = 50
    inbetweenDelay = 2

    m.Move(0, 75,speed)

    time.sleep(inbetweenDelay)

    m.Move(270,110,speed)

    time.sleep(inbetweenDelay)

    m.Move(180,75,speed)

    time.sleep(inbetweenDelay)

    m.Move(90,110,speed)

    time.sleep(inbetweenDelay)
    break
