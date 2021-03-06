from Wheel import Wheel

import IODefinitions as ios


class Machine():

    def __init__(self):
        self.front_left = Wheel(ios.FL_PWM, ios.FL_DirF, ios.FL_DirB, ios.FL_EnA, ios.FL_EnB)
        self.front_right = Wheel(ios.FR_PWM, ios.FR_DirF, ios.FR_DirB, ios.FR_EnA, ios.FR_EnB)
        self.back_left = Wheel(ios.BL_PWM, ios.BL_DirF, ios.BL_DirB, ios.BL_EnA, ios.BL_EnB)
        self.back_right = Wheel(ios.BR_PWM, ios.BR_DirF, ios.BR_DirB, ios.BR_EnA, ios.BR_EnB)

    def Move(self, direction_platform, distance, speed):
        self.front_left.Move(direction_platform, distance, speed)
        self.front_right.Move(direction_platform, distance, speed)