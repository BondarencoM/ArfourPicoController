from Wheel import Wheel

import IODefinitions as ios
import time

POLL_DELAY = 0.001

class Machine():

    def __init__(self):
        self.front_left = Wheel(ios.FL_PWM, ios.FL_DirF, ios.FL_DirB, ios.FL_EnA, ios.FL_EnB)
        self.front_right = Wheel(ios.FR_PWM, ios.FR_DirF, ios.FR_DirB, ios.FR_EnA, ios.FR_EnB)
        self.back_left = Wheel(ios.BL_PWM, ios.BL_DirF, ios.BL_DirB, ios.BL_EnA, ios.BL_EnB)
        self.back_right = Wheel(ios.BR_PWM, ios.BR_DirF, ios.BR_DirB, ios.BR_EnA, ios.BR_EnB)

    def Move(self, direction_platform, distance, speed):

        if direction_platform == 0:
            self.front_left.Move(True, distance, speed)
            self.front_right.Move(True, distance, speed)
            self.back_left.Move(True, distance, speed)
            self.back_right.Move(True, distance, speed)

            while not self.UpdateAll():
                time.sleep(POLL_DELAY)

        if direction_platform == 90:
            self.front_left.Move(False, distance, speed)
            self.front_right.Move(True, distance, speed)
            self.back_left.Move(True, distance, speed)
            self.back_right.Move(False, distance, speed)

            while not self.UpdateAll():
                time.sleep(POLL_DELAY)

        if direction_platform == 180:
            self.front_left.Move(False, distance, speed)
            self.front_right.Move(False, distance, speed)
            self.back_left.Move(False, distance, speed)
            self.back_right.Move(False, distance, speed)

            while not self.UpdateAll():
                time.sleep(POLL_DELAY)

        if direction_platform == 270:
            self.front_left.Move(True, distance, speed)
            self.front_right.Move(False, distance, speed)
            self.back_left.Move(False, distance, speed)
            self.back_right.Move(True, distance, speed)

            while not self.UpdateAll():
                time.sleep(POLL_DELAY)

    def Stop(self):
        self.front_left.Move(True, 0, 0)
        self.front_right.Move(False, 0, 0)
        self.back_left.Move(False, 0, 0)
        self.back_right.Move(True, 0, 0)
    
    def UpdateAll(self):
        return self.front_left.Update() and self.front_right.Update() and self.back_left.Update() and self.back_right.Update()