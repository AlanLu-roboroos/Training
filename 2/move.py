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


kP = 5

startSpeed = 20
acceleration = 200
        
def getSpeed(distance):
    return round(umath.sqrt(startSpeed**2 + 2*acceleration*distance))

def moveDist(distance):
    hub.imu.reset_heading(0)
    drive_speed = 10

    drive.reset()
    timer.reset()
    timer.resume()

    print("Time, Distance, Speed")

    while distance > drive.distance():
        heading = hub.imu.heading()

        isFirstHalf = drive.distance() < (distance / 2)

        # Method - By Time
        ##################################################
        if isFirstHalf:
            drive_speed = round(umath.sqrt(startSpeed**2 + 2*acceleration*drive.distance()))
        else:
            drive_speed = round(umath.sqrt(startSpeed**2 + 2*acceleration*(distance - drive.distance())))

        # Method - By Loop
        ##################################################
        # if isFirstHalf:
        #     drive_speed += 5
        # else:
        #     drive_speed -= 5

        # Method - By Distance
        ##################################################
        # if isFirstHalf:
        #     drive_speed = drive.distance() * 5 + 10
        # else:
        #     drive_speed = (distance - drive.distance()) * 5 + 10

        steering = -heading * kP
        drive.drive(drive_speed, steering)
        print(timer.time(), ", ", drive.distance(),  ", " , drive_speed, sep="")

moveDist(500)