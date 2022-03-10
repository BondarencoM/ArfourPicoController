from Motor import Motor
import rotaryio
import math


class Wheel:
    def __init__(self, pwmDrive, dirF, dirB, encA, encB):
        
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runEncoder.position
        self.runMotor = Motor(pwmDrive, dirF, dirB)
        self.pulsesPerCentim = 155 / (7.92 * math.pi)

    def Move(self, forward, distance, speed):
        pulses = distance * self.pulsesPerCentim
        print (pulses)
        self.desiredPosition = self.runEncoder.position + (pulses * (1 if forward else -1))
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

    def PulsesTo(self, forward, distance, speed):
        if forward == 1:
            
            self.pulses = self.distance / self.distance_per_pulse
            set_pulses = self.runEncoder.position
            EncA_Pulses_after_distance = self.runEncoder.position + self.pulses
            self.runMotor.Move(forward, speed)
            if EncA_Pulses_after_distance == set_pulses:
                self.runMotor.Move(0, 0)
            
        if forward == 0:
            self.pulses = self.distance / self.distance_per_pulse
            set_pulses = self.runEncoder.position
            EncA_Pulses_after_distance = self.runEncoder.position - self.pulses
            self.runMotor.Move(forward, speed)
            if EncA_Pulses_after_distance != set_pulses:
                self.runMotor.Move(0, 0)
