from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.imu.reset_heading(0)

wait(200)

while True:
    if hub.imu.heading() > 5:
        hub.display.icon(Icon.ARROW_RIGHT)
    elif hub.imu.heading() < -5:
        hub.display.icon(Icon.ARROW_LEFT)
    else:
        hub.display.icon(Icon.HAPPY)

    if len(hub.buttons.pressed()) > 0:
        hub.display.icon(Icon.CIRCLE)
        hub.imu.reset_heading(0)