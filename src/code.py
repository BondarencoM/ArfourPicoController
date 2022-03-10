# The imports of all used libraries
import time
import usb_cdc

## Setup
serial = usb_cdc.console

## Loop
while True:
    # when the connection is there
    if serial.connected:
        # when there is new data
        if serial.in_waiting == 4:
            # how many bytes?
            print("Bytes to read:   ", serial.in_waiting)

            # read the first byte
            command_byte = serial.read(1)
            print("First byte:      ", command_byte)

    time.sleep(1)
