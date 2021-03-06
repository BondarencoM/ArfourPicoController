from digitalio import DigitalInOut

class Motor():

    def __init__(self, pwmDrive, dirF, dirB):
        self.PWM_drive = pwmDrive
        self.Forward = dirF
        self.Backward = dirB

    def Move(self, direction_wheel, speed=0):
        self.Forward.value = direction_wheel
        self.Backward.value = not direction_wheel

        self.PWM_drive.duty_cycle = int((2 ** 16 -1) * speed / 100)


