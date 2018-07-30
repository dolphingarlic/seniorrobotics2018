"""A simple Robot class for the EV3 robots"""

from ev3dev.auto import *


class Robot(object):
    """A Robot class that emulates the EV3 robots

    This is a Robot class created for the SJC Robotics team
    to try to emulate the EV3 robots' non-Python capabilities
    like moving forwards, getting the colour etc.

    Attributes:
        grabber: The grabbing claw that picks up the lego 'food' block
        left_colour_sensor: Colour Sensor in port 1
        right_colour_sensor: Colour Sensor in port 4
        left_wheel: The motor for the left wheel
        right_wheel: The motor for the right wheel
    """

    def __init__(self):
        self.grabber = Motor(OUTPUT_C)
        self.arm = Motor(OUTPUT_B)
        self.left_colour_sensor = ColorSensor(address='3')
        self.right_colour_sensor = ColorSensor(address='2')
        self.inner_colour_sensor = ColorSensor(address='1')
        self.outer_colour_sensor = ColorSensor(address='4')
        self.left_wheel = Motor(OUTPUT_D)
        self.right_wheel = Motor(OUTPUT_A)

    def move_straight(self, time, speed, direction):
        """Moves the robot straight for a given time"""

        if direction.upper() == 'BACKWARDS':
            self.left_wheel.run_timed(time_sp=time, speed_sp=speed)
            self.right_wheel.run_timed(time_sp=time, speed_sp=speed)
        elif direction.upper() == 'FORWARDS':
            self.left_wheel.run_timed(time_sp=time, speed_sp=-speed)
            self.right_wheel.run_timed(time_sp=time, speed_sp=-speed)

    #def follow_black_line(self):

    def turn(self, direction):
        """Turns the robot 90 degrees in a given direction"""
        if direction.upper() == 'LEFT':
            self.left_wheel.run_to_rel_pos(position_sp=720, speed_sp=500)
        elif direction.upper() == 'RIGHT':
            self.right_wheel.run_to_rel_pos(position_sp=720, speed_sp=500)

    def grab(self):
        """Makes the grabber grab the food brick"""
        self.grabber.run_to_rel_pos(position_sp=-540, speed_sp=1000)

    def release(self):
        """Makes the grabber release the food brick"""
        self.grabber.run_to_rel_pos(position_sp=540, speed_sp=1000)

    def scan(self, colour_sensor):
        """Returns the colour that the color sensor senses"""
        return colour_sensor.color