from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

while True:
    print("pitch:", hub.imu.tilt()[0], ";", "roll:", hub.imu.tilt()[1], ";", "heading:", round(hub.imu.heading()))
