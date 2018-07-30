#!/usr/bin/env python3

from time import sleep
from src.robot import Robot

robot = Robot()
robot.move_straight(1000, 1000, 'Forwards')
robot.left_wheel.wait_until_not_moving()
robot.turn('Left')

while True:
    print(robot.scan(robot.outer_colour_sensor))
    sleep(0.5)