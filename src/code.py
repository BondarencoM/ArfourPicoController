from Machine import Machine
import time
print("Starting")
m = Machine()
while True:
    speed = 25
    inbetweenDelay = 0.5

    m.Move(0,-1,speed)
    time.sleep(2)

    m.Move(0,0,0)
    time.sleep(inbetweenDelay)

    m.Move(270,-1,speed)
    time.sleep(2)

    m.Move(0,0,0)
    time.sleep(inbetweenDelay)

    m.Move(180,-1,speed)
    time.sleep(2)

    m.Move(0,0,0)
    time.sleep(inbetweenDelay)

    m.Move(90,-1,speed)
    time.sleep(2)
