"""A simple Robot class for the EV3 robots"""

from ev3dev.auto import *


class Robot(object):
    """A Robot class that emulates the EV3 robots

    This is a Robot class created for the SJC Robotics team
    to try to emulate the EV3 robots' non-Python capabilities
    like moving forwards, getting the colour etc.

    Attributes:
        grabber: The grabbing claw that picks up the lego 'food' block
        colour_sensor1: Colour Sensor in port 1
        colour_sensor2: Colour Sensor in port 4
        left_wheel: The motor for the left wheel
        right_wheel: The motor for the right wheel
    """

    def __init__(self):
        self.grabber = MediumMotor('outB')
        self.colour_sensor1 = ColorSensor(address='1')
        self.colour_sensor2 = ColorSensor(address='4')
        self.left_wheel = Motor(OUTPUT_A)
        self.right_wheel = Motor(OUTPUT_B)

    def move_forwards(self, time, speed):
        """Moves the robot straight forwards for a given time"""
        self.left_wheel.runTimed(time_sp=time, speed_sp=speed)
        self.right_wheel.runTimed(time_sp=time, speed_sp=speed)

    def turn(self, direction):
        """Turns the robot 90 degrees in a given direction"""
        if direction.upper() == 'LEFT':
            self.left_wheel.run_to_rel_pos(position_sp=360, speed_sp=1000)
        elif direction.upper() == 'RIGHT':
            self.right_wheel.run_to_rel_pos(time_sp=360, speed_sp=1000)

    def grab(self):
        """Makes the grabber grab the food brick"""
        self.grabber.run_to_rel_pos(position_sp=-540, speed_sp=1000)

    def release(self):
        """Makes the grabber release the food brick"""
        self.grabber.run_to_rel_pos(position_sp=540, speed_sp=1000)
