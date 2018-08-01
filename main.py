#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *
Pos = (1, 2, 3, 4)
Dis = (1, 2, 3, 4)
Rot = ('LEFT','RIGHT','RIGHT','LEFT')
SPEED = 100


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
'''

"""Actual pathfinding"""
ROBOT.move_to(A1C4)
for y in range(0,4):
    for x in range(0,4):
        ROBOT.move_straight_degrees(Pos[x], SPEED, 1)
        ROBOT.turn(Rot[x])
        ROBOT.move_straight_degrees(Dis[x], SPEED, 1)
        if 2 <= ROBOT.outer_colour_sensor.color <= 5:
            ROBOT.drop()
            ROBOT.grab()
            # do reverse of previous actions
            # backtrack to factory area
            break
        ROBOT.move_straight_degrees(Dis[x], SPEED, -1)
        back_rotate = 'LEFT'
        if Rot[x] == 'LEFT':
            back_rotate = 'RIGHT'
        ROBOT.turn(back_rotate)
        
        # continue to node
