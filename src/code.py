# The imports of all used libraries
import IODefinitions
import usb_cdc

## Setup
serial = usb_cdc.Serial


## Single run
print("test: " )
print(not not serial.connected)

## Loop
while True:
    pass  # does nothing
