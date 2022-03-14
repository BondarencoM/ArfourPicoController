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
last_command = [None]

should_execute = True

## Loop
while True:
    # check for updates
    current_command = comms.update_command()

    if current_command != last_command:
        should_execute= True
        last_command = current_command

    # only when ther is a command
    if current_command and current_command is not []:

        if current_command[0] != 'stop':
           print(current_command)

        if current_command[0] == "stop" and should_execute:
            m.Stop()
            should_execute = False

        # when move_10m
        if current_command[0] == "move_10m" and should_execute:
            direction = current_command[1]  # 0 degrees
            speed = current_command[2]      # 50%
            m.Move(direction, 465, speed)
            should_execute = False

        # when move_1m
        if current_command[0]== "move_1m":
            direction = current_command[1]  ## angle in degrees
            speed = current_command[2]      ## 50%

            if direction == 0 and should_execute:
                # move 1 meter forward
                m.Move(direction, 75, speed)
                should_execute = False

            if direction == 270 and should_execute:
                # move 1 meter to the right
                m.Move(direction, 110, speed)
                should_execute = False

            if direction == 180 and should_execute:
                # move 1 meter backwards
                m.Move(direction, 75, speed)
                should_execute = False

            if direction == 90 and should_execute:
                # move 1 meter to the left
                m.Move(direction, 110, speed)
                should_execute = False

    # done with this command, so save to last command
    last_command = current_command
