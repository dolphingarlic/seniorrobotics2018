#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.map_nodes import *

ROBOT = Robot()

ROBOT.follow_until_next_node()
