from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import umath

hub = PrimeHub()

# v**2 = u**2 + 2as - Formula for speed

leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.D, Direction.CLOCKWISE)

drive = DriveBase(leftMotor, rightMotor, 56, 112)

acceleration = 400
startSpeed = 20
turn_correction = 6

def getSpeed(distance):
    return round(umath.sqrt(startSpeed**2 + 2*acceleration*distance))

def turnAngle(angle):
    return (angle - hub.imu.heading() + 180) % 360 - 180

def getHeading():
    return (hub.imu.heading() + 180) % 360 - 180

def moveDist(distance, speed, heading=None, up=True, down=True, timeout=10000):
    distance = abs(distance)

    drive.reset()

    if heading == None:
        heading = getHeading()
    
    while True:
        curr_distance = abs(drive.distance())
        if curr_distance > distance:
            break
        
        firstHalf = curr_distance < distance / 2

        if not up and firstHalf:
            drive_speed = speed
        elif not down and not firstHalf:
            drive_speed = speed
        else:
            if firstHalf:
                drive_speed = getSpeed(curr_distance)
            else:
                drive_speed = getSpeed(distance - curr_distance)
        drive_speed = min(speed, drive_speed)

        drive.drive(drive_speed, turnAngle(heading) * turn_correction)
    drive.stop()


moveDist(400, 400)