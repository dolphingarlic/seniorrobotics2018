#!/usr/bin/env python3

from time import sleep
from typing import Dict

from src.robot import Robot
from src.map_nodes import *

"""Fields and constants"""
# Stage 1
Pos_crate = (1, 2, 3, 4)
Dis_crate = (1, 2, 3, 4)
Rot_crate = ('LEFT', 'RIGHT', 'RIGHT', 'LEFT')
STAGE_1_NODE_COUNT = {0: 3, 1: 2, 2: 2, 3: 1}
# Stage 2
Pos_cover = (1, 2, 3, 4)  # Blue, green, yellow, red
# Main
SPEED = 100
COLOURS: Dict[int, str] = {2: "B", 3: "G", 4: "Y", 5: "R"}
current_colour = ""
ROBOT = Robot()

"""Methods in direct relation to path-finding / highest level of logic"""


def backtrack_to_nearest_node(pos):
    ROBOT.move_straight_degrees(Dis_crate[pos], SPEED, -1)
    back_rotate = 'LEFT'
    if Rot_crate[pos] == 'LEFT' or pos == 2:
        back_rotate = 'RIGHT'
    ROBOT.turn(back_rotate)
    if x == 2:  # special case for transition between p2 and p3
        ROBOT.follow_until_next_node()
        ROBOT.turn('AROUND')
    else:
        ROBOT.follow_until_next_node()
        ROBOT.turn('LEFT')


"""Actual path finding"""
ROBOT.move_to(A1C4)
for y in range(0, 4):
    x = 0
    """Stage 1 - Collection and detection of container"""
    for x in range(y, 4):
        ROBOT.move_straight_degrees(Pos_crate[x], SPEED, 1)
        ROBOT.turn(Rot_crate[x])
        ROBOT.move_straight_degrees(Dis_crate[x], SPEED, 1)
        """On detect of a block"""
        if 2 <= ROBOT.outer_colour_sensor.color <= 5:
            ROBOT.drop()
            ROBOT.grab()
            backtrack_to_nearest_node(x)
            current_colour = COLOURS[ROBOT.outer_colour_sensor.color]
            break
        backtrack_to_nearest_node(x)
    "Go to C1"
    if x == 2:
        ROBOT.move_straight_degrees(Pos_crate[2], SPEED, 1)
        #  TODO: Follow until next node with a slight delay before stopping
    for l in range(0, STAGE_1_NODE_COUNT[x]):
        ROBOT.follow_until_next_node()
        ROBOT.turn('LEFT')
    """Stage 2 - top thing + block (It's shit, but so is the entire codebase)"""
    if current_colour == "Y" or current_colour == "B":
        ROBOT.move_to(C1C4)
        if current_colour == "B":
            ROBOT.turn('RIGHT')
            ROBOT.move_straight_degrees(Pos_cover[0], SPEED, 1)
            ROBOT.turn('RIGHT')
            ROBOT.take_lid_and_place_box()
            # TODO: reverse until black line detected
            ROBOT.turn('LEFT')
            ROBOT.follow_until_next_node()
            ROBOT.move_to(C4D1)
        else
            ROBOT.turn('LEFT')
            ROBOT.move_straight_degrees(Pos_cover[2], SPEED, 1)
            ROBOT.turn('LEFT')
            ROBOT.take_lid_and_place_box()
            # TODO: reverse until black line detected
            ROBOT.turn('LEFT')
            ROBOT.follow_until_next_node()
            ROBOT.move_to(C4D1)
    elif current_colour == "G":
        





