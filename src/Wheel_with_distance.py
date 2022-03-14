from Motor import Motor
import rotaryio
import math


class Wheel:
    def __init__(self, pwmDrive, dirF, dirB, encA, encB):
        self.runEncoder = rotaryio.IncrementalEncoder(encA, encB)
        self.runEncoder.position
        # self.runEncoder.position = EncA_Pulses
        self.runMotor = Motor(pwmDrive, dirF, dirB)
        self.distance_per_pulse = self.Diameter * math.pi() / 155

    #   def calculate_RPM(self,EncA_Pulses):
    #         if EncA_Pulses = not EncA_Pulses_New:
    #             Time_1 =current_milli_time()
    #             EncA_Pulses_New = EncA_Pulses
    #         if EncA_Pulses_New = not EncA_Pulses_Old :
    #             Delta_Time=Time_1-Time_2
    #             self.Delta_pulses = EncA_Pulses_New - EncA_Pulses_Old
    #             self.Rotations = Delta_pulses / 155
    #             self.RPS=Rotations /Delta_Time
    #             self.EncA_Pulses_Old =  self.EncA_Pulses_New
    #              Time_2 =current_milli_time()

    def Move(self, forward, distance, speed):
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
            if EncA_Pulses_after_distance != set_pulses:
                self.runMotor.Move(forward, speed)
            self.runMotor.Move(0, 0)
