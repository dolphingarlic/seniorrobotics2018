#!/usr/bin/env python3

from time import sleep
from src.robot import Robot
from src.node import node

robot = Robot()
robot.move_straight(1000, 1000, 'Forwards')
robot.left_wheel.wait_until_not_moving()
robot.turn('Left')
robot.left_wheel.wait_until_not_moving()
robot.turn('Right')

for i in range(100):
    print(robot.scan(robot.outer_colour_sensor))
    sleep(0.5)

A1 = node("A1", "", "B1", "", "B2")
B1 = node("B1", "", "", "C1", "A1")
B2 = node("B2", "", "A1", "C4", "")
C1 = node("C1", "B1", "", "D1", "C2")
C2 = node("C2", "G", "C1", "R", "C3")
C3 = node("C3", "B", "C2", "Y", "C4")
C4 = node("C4", "B2", "C3", "D3", "")
D1 = node("D1", "C1", "", "D1", "D2")
D2 = node("D2", "", "D1", "", "D3")
D3 = node("D3", "C4", "D2", "E3", "")
E1 = node("E1", "D1", "", "", "E2")
E2 = node("E2", "", "E1", "F4", "E3")
E3 = node("E3", "D3", "E2", "", "")
F1 = node("F1", "", "", "1", "F2")
F2 = node("F2", "", "F1", "2", "F3")
F3 = node("F3", "", "F2", "3", "F4")
F4 = node("F4", "E2", "F3", "", "F5")
F5 = node("F5", "", "F4", "4", "F6")
F6 = node("F6", "", "F5", "5", "F7")
F7 = node("F7", "F6", "", "6", "")

nodes = [A1, B1, B2, C1, C2, C3, C4, D1, D2, D3, E1, E2, E3, F1, F2, F3, F4, F5, F7]


A1D2 = [A1, B1, C1, D1, D2]
D2C2 = [D2, D1, C1, C2]
D2C3 = [D2, D3, C4, C3]
C3E1 = [C3, C2, C1, D1, E1]
C2E1 = [C2, C1, D1, E1]
E3D2 = [E3, D3, D2]
E3A1 = [E3, D3, C4, B2, A1]
