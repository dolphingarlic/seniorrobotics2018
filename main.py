#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *

def take_lid_and_place_box(robot):
    robot.lift()
    robot.arm.wait_until_not_moving()
    robot.move_straight_degrees(235, 300)
    robot.left_wheel.wait_until_not_moving()
    sleep(2)
    robot.move_straight_degrees(-235, 300)

ROBOT = Robot()

'''
for i in range(50):
    print("Right: "+str(ROBOT.right_colour_sensor.reflected_light_intensity))
    print("Left: "+str(ROBOT.left_colour_sensor.reflected_light_intensity))
    sleep(0.5)

"""Actual pathfinding"""
ROBOT.move_to(A1C4)
'''

take_lid_and_place_box(ROBOT)
