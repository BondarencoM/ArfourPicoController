# The imports of all used libraries
import IODefinitions
import time
import usb_cdc

## Setup
serial = usb_cdc.console

## Loop
while True:
    # when the connection is there
    if serial.connected:
        # when there is new data
        if serial.in_waiting:
            print(serial.in_waiting)
            byte_in = serial.read(1)
            print(byte_in)
            

            # probably a state machine
            # when the first byte means to move
            if byte_in == 99:
                # do something
                print("move")


    time.sleep(1)
