#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *

def take_lid_and_place_box(robot):
    robot.lift()
    robot.move_straight_degrees(235, 500, 'FORWARDS')
    robot.move_straight_degrees(-235, 500, 'FORWARDS')

ROBOT = Robot()

for i in range(50):
    print("Right: "+str(ROBOT.right_colour_sensor.reflected_light_intensity))
    print("Left: "+str(ROBOT.left_colour_sensor.reflected_light_intensity))
    sleep(0.5)

