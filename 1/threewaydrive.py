from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.imu.reset_heading(0)


leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.D, Direction.CLOCKWISE)

drive = DriveBase(leftMotor, rightMotor, 56, 112)
drive.drive(200, 0)

turn_amount = 80
tolerance = 2

wait(200)

while True:
    if hub.imu.heading() > tolerance:
        drive.drive(200, -turn_amount)

    elif hub.imu.heading() < -tolerance:
        drive.drive(200, turn_amount)

    else:
        drive.drive(200, 0)