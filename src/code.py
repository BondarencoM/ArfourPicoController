# The imports of all used libraries
import IODefinitions
import time
import usb_cdc

## Setup
serial = usb_cdc.console

## Loop
while True:
    if serial.connected:
        if serial.in_waiting:
            print(serial.connected)
            print(serial.in_waiting)
            serial.read(serial.in_waiting)

    time.sleep(1)
