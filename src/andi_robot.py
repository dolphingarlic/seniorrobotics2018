"""A simple Robot class for the EV3 robots"""

from ev3dev.auto import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, ColorSensor


class Robot(object):
    """A Robot class that emulates the EV3 robots

    This is a Robot class created for the SJC Robotics team
    to try to emulate the EV3 robots' non-Python capabilities
    like moving forwards, getting the colour etc.

    Attributes:
        grabber: The grabbing claw that picks up the lego 'food' block
        arm: The arm that picks up the lid
        left_colour_sensor: Colour Sensor in port 2
        right_colour_sensor: Colour Sensor in port 3
        inner_colour_sensor: Colour Sensor that senses box colour
        outer_colour_sensor: Colour Sensor that senses ship colour
        left_wheel: The motor for the left wheel
        right_wheel: The motor for the right wheel
    """

    COLORS = {0: 'NONE', 2: 'BLUE', 3: 'GREEN', 4: 'YELLOW', 5: 'RED'}

    def __init__(self):
        self.grabber = Motor(OUTPUT_C)
        self.arm = Motor(OUTPUT_B)
        self.left_colour_sensor = ColorSensor(address='3')
        self.right_colour_sensor = ColorSensor(address='4')
        self.inner_colour_sensor = ColorSensor(address='1')
        self.outer_colour_sensor = ColorSensor(address='2')
        self.left_wheel = Motor(OUTPUT_A)
        self.right_wheel = Motor(OUTPUT_D)

    def move_straight_degrees(self, degrees, direction='FORWARDS'):
        """Moves the robot straight for the degrees specified"""

        self.left_wheel.run_to_rel_pos(position_sp=(-1)**(direction=='FORWARDS')*degrees, speed_sp=300)
        self.right_wheel.run_to_rel_pos(position_sp=(-1)**(direction=='FORWARDS')*degrees, speed_sp=300)
        self.left_wheel.wait_until_not_moving()

    def turn(self, direction, degrees=90):
        """Turns the robot n degrees in a given direction"""
        if direction.upper() == 'LEFT':
            self.left_wheel.run_to_rel_pos(position_sp=degrees*8/3, speed_sp=300)
            self.right_wheel.run_to_rel_pos(position_sp=-degrees*8/3, speed_sp=300)

        elif direction.upper() == 'RIGHT':
            self.left_wheel.run_to_rel_pos(position_sp=-degrees*8/3, speed_sp=300)
            self.right_wheel.run_to_rel_pos(position_sp=degrees*8/3, speed_sp=300)

        self.left_wheel.wait_until_not_moving()

    def grab(self):
        """Makes the grabber grab the food brick"""
        self.grabber.run_to_rel_pos(position_sp=-540, speed_sp=1000)
        self.grabber.wait_until_not_moving()

    def release(self):
        """Makes the grabber release the food brick"""
        self.grabber.run_to_rel_pos(position_sp=540, speed_sp=1000)
        self.grabber.wait_until_not_moving()

    def lift_arm(self):
        """Lifts the arm to grab the lid"""
        self.arm.run_to_rel_pos(position_sp=-120, speed_sp=500, state='holding')
        self.arm.wait_until_not_moving()

    def drop_arm(self):
        """Drops the arm to secure the container"""
        self.arm.run_to_rel_pos(position_sp=120, speed_sp=500)
        self.arm.wait_until_not_moving()