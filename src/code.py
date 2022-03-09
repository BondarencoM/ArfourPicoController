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
            # how many bytes?
            print("Bytes to read:   ", serial.in_waiting)

            # read the first byte
            command_byte = serial.read(1)
            print("First byte:      ", command_byte)
            
            # how many bytes left?
            print("Bytes left:      ", serial.in_waiting)

            # read the second byte
            second_byte = serial.read(1)
            print("Second byte: ", second_byte)
            
            # how many bytes left?
            print("Bytes left:      ", serial.in_waiting)

            # probably a state machine
            # when the first byte means to move
            if command_byte == 99:
                # do something
                print("command move")

            # clear buffer
            serial.reset_input_buffer()

            # and see if anything is left
            print("Bytes left:      ", serial.in_waiting)

    time.sleep(1)
