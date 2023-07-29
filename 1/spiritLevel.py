from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

lastLeftRight = 0
lastUpDown = 0

def limit(val, maximum, minimum):
    return min(max(val, maximum), minimum)

hub.display.off()
hub.display.pixel(2, 2, 100)
while True:
    leftRight, upDown = hub.imu.tilt()

    leftRight = limit(round(leftRight / 10), -2, 2) + 2
    upDown = limit(-round(upDown / 10), -2, 2) + 2

    # print(leftRight, upDown)

    if leftRight != lastLeftRight or upDown != lastUpDown:
        hub.display.off()
        hub.display.pixel(leftRight, upDown, 100)

    lastLeftRight = leftRight
    lastUpDown = upDown