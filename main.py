#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *


def take_lid_and_place_box(robot):
    robot.lift()
    robot.move_straight_degrees(235, 500)
    robot.move_straight_degrees(-235, 500)

print("Started")
ROBOT = Robot()
print("Running wheels")
ROBOT.left_wheel.run_direct(duty_cycle_sp=-80)
ROBOT.right_wheel.run_direct(duty_cycle_sp=-80)
sleep(10)
ROBOT.stop()
print("Stopped")
sleep(2)
print("following")
ROBOT.follow_until_next_node()
