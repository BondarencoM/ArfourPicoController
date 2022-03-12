# imports
import usb_cdc

# Communication Class
class Protocol:
    ## "Private Variables"
    # value to check for when searching for data
    waiting_poss = 2

    # sent data storage
    command = None
    direction = None
    speed = None
    distance = None

    commandList = []
    prevCommandList = []

    # encoding values
    max_direction = 359
    max_speed = 100

    ## "Public Funtions"
    # Initialition
    def __init__(self):
        self.serial = usb_cdc.data
        self.commandList = [None]

    # function to get the new orders
    def update_command(self):
        # when the connection is there
        if self.serial.connected:
            # save previous list
            self.prevCommandList = self.commandList

            # when there is new data
            if self.serial.in_waiting > self.waiting_poss:
                # clear the current list
                self.commandList = [None]

                # how many bytes?
                print("Bytes to read:   ", self.serial.in_waiting)

                # read the first byte
                command_byte = self.serial.read(1)
                print("Command byte:    ", command_byte)
                self.command = self.command_decode(command_byte)
                #self.serial.write(f"Command byte: {command_byte}".encode())

                if self.command == "stop":
                    self.commandList = [self.command]

                    # send the list to machine
                    return self.commandList

                # when the command means to move, there should be 4 bytes of data in total
                elif self.command == "move" and self.serial.in_waiting > 2:
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
                    distance_byte = self.serial.read(2)
                    print("Distance byte:  ", distance_byte)
                    # decode distance back to cm
                    self.distance = self.bytes_decode(distance_byte)

                    # there should be no bytes left
                    print(self.serial.in_waiting, " bytes are left")
                    self.serial.reset_input_buffer()

                    # set values in list
                    self.commandList = [self.command, self.direction, self.speed, self.distance]

                    # send the list to machine
                    return self.commandList

                # but when the command means to rotate, there should only be 3 bytes of data in total
                elif self. command == "rotate" and self.serial.in_waiting > 1:
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

                    # there should be no bytes left
                    print(self.serial.in_waiting, " bytes are left")
                    self.serial.reset_input_buffer()

                    # set values in list
                    self.commandList = [self.command, self.direction, self.speed]

                    # send the list to machine
                    return self.commandList
                
                # but when the command means to move 10 meters staight, there should be 4 bytes of data in total
                elif self. command == "move_10m" and self.serial.in_waiting > 2:
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
                    distance_byte = self.serial.read(2)
                    print("Distance byte:  ", distance_byte)
                    # decode distance back to cm
                    self.distance = self.bytes_decode(distance_byte)

                    # there should be no bytes left
                    print(self.serial.in_waiting, " bytes are left")
                    self.serial.reset_input_buffer()

                    # set values in list
                    self.commandList = [self.command, self.direction, self.speed, self.direction]

                    # send the list to machine
                    return self.commandList

                # but when the command means to move 1 meter staight, there should be 4 bytes of data in total
                elif self. command == "move_1m" and self.serial.in_waiting > 2:
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
                    distance_byte = self.serial.read(2)
                    print("Distance byte:  ", distance_byte)
                    # decode distance back to cm
                    self.distance = self.bytes_decode(distance_byte)

                    # there should be no bytes left
                    print(self.serial.in_waiting, " bytes are left")
                    self.serial.reset_input_buffer()

                    # set values in list
                    self.commandList = [self.command, self.direction, self.speed, self.direction]

                    # send the list to machine
                    return self.commandList

                # when finding absolutely garbage, just delete that
                else:
                    self.serial.reset_input_buffer()

            # send the previous list again, since there are no changes
            return self.prevCommandList


    ## "Private Functions"
    # function to decode command byte
    def command_decode(self, comm = None):
#         comm = int.from_bytes(comm, "big")
#         print(comm)
        if comm == b"\x00":
            self.waiting_poss = 0
            return "stop"
        elif comm == b"\x01":
#             print("Move")
            self.waiting_poss = 2
            return "move"
        elif comm == b"\x02":
            self.waiting_poss = 2
            return "rotate"
        elif comm == b"\x03":
            self.waiting_poss = 2
            return "move_10m"
        elif comm == b"\x04":
            self.waiting_poss = 2
            return "move_1m"
        
        elif comm > b"\x04":
            self.waiting_poss = 0
            return None

    # function to decode the bytes to original values
    def byte_decode(self, byte, max_value = 100):
        byte = int.from_bytes(byte, "big")
        # print(byte)
        max_byte_val = 255
        # undo de encoding of the byte using the parameters values
        return round(byte * max_value / max_byte_val)

    # function to decode the bytes to original values
    def bytes_decode(self, byte):
#         print("HERE")
        byte = int.from_bytes(byte, "big")
#         print(byte)
        return byte
