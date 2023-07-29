from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import umath

hub = PrimeHub()

leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.D, Direction.CLOCKWISE)

drive = DriveBase(leftMotor, rightMotor, 56, 112)

timer = StopWatch()

startSpeed = 20
acceleration = 3

def turn(angle):
    turn_angle = angle - hub.imu.heading()
    while abs(turn_angle) > 1:


        # turn_angle = angle - hub.imu.heading()

        turn_angle = (angle - hub.imu.heading() + 180) % 360 - 180


        # turn_speed = turn_angle * 3 + 20

        turn_speed = turn_angle * acceleration + umath.copysign(startSpeed, turn_angle)

        drive.drive(0, turn_speed)

        print(turn_angle, turn_speed)
    drive.stop()

turn(90)

raise KeyboardInterrupt