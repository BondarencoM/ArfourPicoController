from Motor import Motor
import rotaryio

class Wheel():

    def __init__(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runMotor = Motor(pwmDrive, dirF, dirB)

    def Move(self, forward, distance, speed):
        self.desiredPosition = self.runEncoder.position + (distance * (1 if forward else -1))
        if forward:
            self.isFinished = lambda : self.runEncoder.position > self.desiredPosition
        else: 
            self.isFinished = lambda : self.runEncoder.position < self.desiredPosition
        self.runMotor.Move(forward, speed)
        

    def Update(self):
        if(self.isFinished()):
            self.runMotor.Move(True, 0)
            return True
        return False