class Motor():

    def __init__(self, pwmDrive, dirF, dirB):
        self.PWM_drive = pwmDrive
        self.Forward = dirF
        self.Backward = dirB

    def Move(self, direction_wheel, output_pid=0):
        self.Forward.value = direction_wheel
        self.Backward.value = not direction_wheel
        self.PWM_drive.duty_cycle = int(output_pid)



