from Machine import Machine
import time
from Wheel import Wheel
print("Starting")
m = Machine()

#m.Move(0, 465, 50)
#m.Move(0, 465, 50)

while True:
    speed = 50
    inbetweenDelay = 2

    m.Move(0, 75,speed)

    time.sleep(inbetweenDelay)

    m.Move(270,110,speed)

    time.sleep(inbetweenDelay)

    m.Move(180,75,speed)

    time.sleep(inbetweenDelay)

    m.Move(90,110,speed)

    time.sleep(inbetweenDelay)
    break
