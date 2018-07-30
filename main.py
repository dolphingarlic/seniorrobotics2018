#!/usr/bin/env python3

from src.robot import Robot

robot = Robot()
robot.move_straight(1000, 1000, 'Forwards')
robot.turn('Left')

while True:
    print(robot.scan())