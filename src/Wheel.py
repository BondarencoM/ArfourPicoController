from Motor import Motor
import rotaryio
import math
import time
from PID import PID


class Wheel:
    def __init__(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runEncoder.position
        self.runMotor = Motor(pwmDrive, dirF, dirB)
        self.pulsesPerCentim = 155 / (7.92 * math.pi)
        self.EncA_Pulses = self.runEncoder.position
        self.Time_2 = 0.0
        self.EncA_Pulses_New = 0
        self.EncA_Pulses_Old = 0
        self.output_pid = 0

    def Move(self, forward, distance, speed, k):
        self.pid = PID(k, 0, 0, setpoint=(speed * 6.25))
        pulses = distance * self.pulsesPerCentim
        self.forward = forward
        #print(pulses)
        self.desiredPosition = self.runEncoder.position + (pulses * (1 if forward else -1))
        if forward:
            self.isFinished = lambda : self.runEncoder.position > self.desiredPosition
        else:
            self.isFinished = lambda : self.runEncoder.position < self.desiredPosition
#         self.runMotor.Move(forward, self.output_pid)

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

    def calculate_RPM(self, wheel):
        if self.runEncoder.position != self.EncA_Pulses_New:
            Time_1 = time.monotonic()
            self.EncA_Pulses_New = self.runEncoder.position
        if self.EncA_Pulses_New != self.EncA_Pulses_Old :
            self.Delta_Time = Time_1 - self.Time_2
            self.Delta_pulses = abs(self.EncA_Pulses_New - self.EncA_Pulses_Old)
            self.Rotations = self.Delta_pulses / 155
            self.RPS = (self.Rotations) / (self.Delta_Time)
            self.RPM = self.RPS * 60
            self.EncA_Pulses_Old = self.EncA_Pulses_New
            self.Time_2 = time.monotonic()
            print(wheel , self.RPM)
        else:
            self.RPM = 0
            print(self.RPM)

    def pid_speed_wheel(self):
        self.output_pid = self.pid(self.RPM)
        #if self.ouput_pid > 65534:
            #self.ouput_pid = 65534
        self.runMotor.Move(self.forward, self.output_pid)
        #print(self.output_pid)

