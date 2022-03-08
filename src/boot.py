# The imports of all used libraries
import usb_cdc

## Setup
serial = usb_cdc.enable(console = False, data = True)
