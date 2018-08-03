#!/usr/bin/env python3

from src.andi_robot import Robot

R = Robot()

START_TO_EDGE = 100
START_TO_FOOD = 500
EDGE_TO_FOOD = 200
FOOD_OFFSET = 20
EDGE_TO_RG = 50
EDGE_TO_YB = 350
FOOD_TO_FACTORY = 300
FOOD_TO_BOAT = 400
DIST_BETWEEN_BOATS = 50
BOAT_TO_SEA = 50

# Move to the centre of the food area from start
R.move_straight_degrees(START_TO_FOOD)

for i in range(4):
    print('Position #{}'.format(i + 1))
    R.turn('Right', 45 + 90 * i)
    R.move_straight_degrees(100 + FOOD_OFFSET * (-1)**i)
    current_color = Robot.COLORS[R.inner_colour_sensor.color]
    if not current_color == 'NONE':
        R.drop_arm()
        R.grab()
        R.turn('Right', 180)
        R.move_straight_degrees(100 + FOOD_OFFSET * (-1)**i)
        R.turn('Left', -45 + 90 * i)
    else:
        R.turn('Right', 180)
        R.move_straight_degrees(100 + FOOD_OFFSET * (-1)**i)
        R.turn('Left', 135 - 90 * i)
        break

    R.move_straight_degrees(200)
    R.turn('Left')

    if current_color == 'YELLOW' or 'RED':
        R.move_straight_degrees(250)
    else:
        R.move_straight_degrees(350)
    R.turn('Left')

    if current_color == 'GREEN' or 'RED':
        R.lift_arm()
        R.move_straight_degrees(EDGE_TO_RG)
        R.move_straight_degrees(EDGE_TO_RG, 'BACKWARDS')
    else:
        R.lift_arm()
        R.move_straight_degrees(EDGE_TO_YB)
        R.move_straight_degrees(EDGE_TO_YB, 'BACKWARDS')
    R.turn('Right')

    R.move_straight_degrees(FOOD_TO_FACTORY + FOOD_TO_BOAT)
    R.turn('Right')

    j = 0

    for j in range(6):
        boat_color = Robot.COLORS[R.outer_colour_sensor.color]
        if boat_color == current_color:
            break
        R.move_straight_degrees(DIST_BETWEEN_BOATS)

    R.turn('Left')
    R.release()
    R.drop_arm()
    R.move_straight_degrees(BOAT_TO_SEA)
    R.move_straight_degrees(BOAT_TO_SEA, 'BACKWARDS')
    R.turn('Right')
    R.move_straight_degrees(DIST_BETWEEN_BOATS * j, 'BACKWARDS')

    R.turn('Right')
    R.move_straight_degrees(FOOD_TO_BOAT)
    R.turn('Left')
    R.move_straight_degrees(EDGE_TO_FOOD)

R.turn('Right', 180)
R.move_straight_degrees(START_TO_FOOD)
print('Success')