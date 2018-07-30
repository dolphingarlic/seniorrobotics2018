#!/usr/bin/env python3

from time import sleep
from src.robot import Robot

robot = Robot()
robot.move_straight(10000, 1000, 'Forwards')
robot.left_wheel.wait_until_not_moving()
robot.right_wheel.wait_until_not_moving()
robot.grab()
robot.grabber.wait_until_not_moving()
sleep(2)
robot.release()