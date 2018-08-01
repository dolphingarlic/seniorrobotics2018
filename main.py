#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *

ROBOT = Robot()

for i in range(50):
    print("Right: "+str(ROBOT.right_colour_sensor.reflected_light_intensity))
    print("Left: "+str(ROBOT.left_colour_sensor.reflected_light_intensity))
    sleep(0.5)

"""Actual pathfinding"""
ROBOT.move_to(A1C4)


