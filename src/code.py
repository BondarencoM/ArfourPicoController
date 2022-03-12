# The imports of all used libraries
import time
from Machine import Machine
from Wheel import Wheel
import protocol

## Setup
print("Starting")
comms = protocol.Protocol()

m = Machine()

current_command = [None]

execute = True

## Loop
while True:
    # check for updates
    current_command = comms.update_command()

    # only when ther is a command
    if current_command is not []:
        # when move_10m
        if current_command[0] == "move_10m" and execute:
            direction = current_command[1]  # 0 degrees
            speed = current_command[3]      # 50% 
            m.Move(direction, 465, speed)

        # when move_1m
        if current_command[0]== "move_1m" and execute:
            direction = current_command[1]  ## angle in degrees
            speed = current_command[2]      ## 50%
            inbetweenDelay = 2

            # move 1 meter forward
            m.Move(direction, 75, speed)    

            time.sleep(inbetweenDelay)

            # move 1 meter to the right
            m.Move(270, 110, speed)

            time.sleep(inbetweenDelay)

            # move 1 meter backwards
            m.Move(180, 75, speed)

            time.sleep(inbetweenDelay)

            # move 1 meter to the left
            m.Move(90, 110, speed)