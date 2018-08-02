#!/usr/bin/env python3

from src.andi_robot import Robot

R = Robot()

R.move_straight_degrees(100)
R.turn('Right')
R.move_straight_degrees(500)
R.turn('Right')
R.move_straight_degrees(200)
R.turn('Right', 45)
R.move_straight_degrees(100)
current_color = Robot.COLORS[R.inner_colour_sensor.color]
if not R.inner_colour_sensor.color == 0:
    R.drop_arm()
    R.grab()
R.turn('Right', 180)
R.move_straight_degrees(100)
R.turn('Left', 45)

R.move_straight_degrees(200)
R.turn('Left')

if current_color == 'YELLOW' or 'RED':
    R.move_straight_degrees(250)
else:
    R.move_straight_degrees(350)
R.turn('Left')

if current_color == 'GREEN' or 'RED':
    R.lift_arm()
    R.move_straight_degrees(50)
    R.move_straight_degrees(50, 'BACKWARDS')
else:
    R.lift_arm()
    R.move_straight_degrees(350)
    R.move_straight_degrees(350, 'BACKWARDS')
R.turn('Right')

R.move_straight_degrees(700)
R.turn('Right')