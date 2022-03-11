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
