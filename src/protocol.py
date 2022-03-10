# Communication Class
from re import S


class Protocol:
    ## "Public Variables"


    ## "Private Variables"
    # sent data storage
    command = None
    direction = None
    speed = None
    distance = None

    listofThings = {command, direction, speed, distance}

    # encoding values
    max_direction = 359 
    max_speed = 100 
    max_distance = 100 

    ## "Public Funtions"
    # Initialition
    def __init__(self):
        self.serial = usb_cdc.console

    # function to get the new orders
    def update_command(self):
        # when the connection is there
        if self.serial.connected:
            # when there is new data
            if self.serial.in_waiting > 2:
                # how many bytes?
                print("Bytes to read:   ", self.serial.in_waiting)

                # read the first byte
                command_byte = self.serial.read(1)
                print("Command byte:      ", command_byte)
                self.command = self.command_decode(command_byte)
                
                if self.serial.in_waiting == 1:
                    # direction fetcher
                    direction_byte = self.serial.read(1)
                    print("Direction byte:  ", direction_byte)
                    # decode direction back to degrees (angle)
                    self.direction = self.byte_decode(direction_byte, self.max_direction)

                    # speed fetcher
                    speed_byte = self.serial.read(1)
                    print("Speed byte:  ", speed_byte)
                    # decode speed back to percent
                    self.speed = self.byte_decode(speed_byte, self.max_speed)
                    
                    # distance fetcher
                    distance_byte = self.serial.read(1)
                    print("Distance byte:  ", distance_byte)
                    # decode distance back to cm
                    self.distance = self.byte_decode(distance_byte, self.max_distance)

                #else if command is 2 there are only 2 bytes waiting

    ## "Private Functions"
    # function to decode command byte
    def command_decode(self, comm = None):
        if comm == 1:
            return "move"
        elif comm == 2:
            return "rotate"
        elif comm > 2:
            return None

    # function to decode the bytes to original values
    def byte_decode(self, byte, max_value = 100):
        max_byte_val = 255
        # undo de encoding of the byte using the parameters values
        return round(byte * max_value / max_byte_val)

