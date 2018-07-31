#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import nodes

ROBOT = Robot()

ROBOT.follow_black_line(5)