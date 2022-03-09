from Motor import Motor
import rotaryio

class Wheel():

    def __init__(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runMotor = Motor(pwmDrive, dirF, dirB)

    def Move(self, direction_platform, distance, speed):
        self.runMotor.Move(True, speed)


