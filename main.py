#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import nodes

ROBOT = Robot()

for i in range(50):
    print("Right: " + ROBOT.right_colour_sensor.reflected_light_intensity)
    print("Left: " + ROBOT.left_colour_sensor.reflected_light_intensity)
    sleep(0.5)

ROBOT.follow_black_line(5)