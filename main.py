#!/usr/bin/env python3

from time import sleep
from src.robot import Robot

robot = Robot()
robot.move_straight(1000, 1000, 'Forwards')
robot.turn('Left')

while True:
    print(robot.scan())
    sleep(0.5)