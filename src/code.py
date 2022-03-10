from Machine import Machine
import time
print("Starting")
m = Machine()
while True:
    speed = 25
    inbetweenDelay = 0.75

    m.Move(0, 155,speed)

    m.Stop()
    time.sleep(inbetweenDelay)

    m.Move(270,155,speed + 10)

    m.Stop()
    time.sleep(inbetweenDelay)

    m.Move(180,155,speed)

    m.Stop()
    time.sleep(inbetweenDelay)

    m.Move(90,155,speed + 10)

    m.Stop()
    time.sleep(inbetweenDelay)
