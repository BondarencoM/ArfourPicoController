from Motor import Motor
import rotaryio

class Wheel():

    def init(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runMotor = Motor(pwmDrive, dirF, dirB)


