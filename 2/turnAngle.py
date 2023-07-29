from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def turnAngle(num):
    return (num + 180) % 360 - 180

def getHeading():
    return turnAngle(hub.imu.heading())

def run():
    while True:
        print(turnAngle(int(input())))

raise KeyboardInterrupt