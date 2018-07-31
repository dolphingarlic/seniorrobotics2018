#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import nodes

robot = Robot()

for i in range(50):
    print(robot.right_colour_sensor.reflected_light_intensity)
    sleep(0.5)