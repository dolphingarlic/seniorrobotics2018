"""A simple Robot class for the EV3 robots"""

from ev3dev.auto import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, ColorSensor
from time import time, sleep


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
    rotation = 'S'
    compass = {'N': 0, 'E': 90, 'S': 180, 'W': -90}

    COLORS = {2: 'BLUE', 3: 'GREEN', 4: 'YELLOW', 5: 'RED'}
    INTENSITY_THRESHOLD = 40
    PROPORTIONAL_THRESHOLD = 75

    def __init__(self):
        self.grabber = Motor(OUTPUT_C)
        self.arm = Motor(OUTPUT_B)
        self.left_colour_sensor = ColorSensor(address='2')
        self.right_colour_sensor = ColorSensor(address='3')
        self.inner_colour_sensor = ColorSensor(address='1')
        self.outer_colour_sensor = ColorSensor(address='4')
        self.left_wheel = Motor(OUTPUT_D)
        self.right_wheel = Motor(OUTPUT_A)
        self.stop_action = "brake"

    def move_straight_degrees(self, degrees, speed):
        """Moves the robot straight for the degrees specified"""
        
        self.left_wheel.run_to_rel_pos(position_sp=degrees, speed_sp=speed)
        self.right_wheel.run_to_rel_pos(position_sp=degrees, speed_sp=speed)

    def move_straight_time(self, move_time, speed, direction):
        """Moves the robot straight for a given time"""

        if direction.upper() == 'BACKWARDS':
            self.left_wheel.run_timed(time_sp=move_time, speed_sp=speed)
            self.right_wheel.run_timed(time_sp=move_time, speed_sp=speed)
        elif direction.upper() == 'FORWARDS':
            self.left_wheel.run_timed(time_sp=move_time, speed_sp=-speed)
            self.right_wheel.run_timed(time_sp=move_time, speed_sp=-speed)

    def stop(self):
        self.right_wheel.stop()
        self.left_wheel.stop()

    def follow_black_line(self, move_time):
        """Makes the robot follow the black line for a period of time"""
        timeout = time() + move_time
        self.move_straight_time(move_time, 500, 'FORWARDS')

        while time() < timeout:
            if self.right_colour_sensor.reflected_light_intensity < Robot.INTENSITY_THRESHOLD:
                self.right_wheel.stop()
                sleep(0.1)
                self.move_straight_time(timeout - time(), 500, 'FORWARDS')
            if self.left_colour_sensor.reflected_light_intensity < Robot.INTENSITY_THRESHOLD:
                self.left_wheel.stop()
                sleep(0.1)
                self.move_straight_time(timeout - time(), 500, 'FORWARDS')

        print('Success!')

    def follow_until_next_node(self):
        """Makes the robot follow the black line for a period of time"""
        print("actually started lmao")

        while True:
            print("got into the while loop")
            self.move_straight_time(1000, 300, 'FORWARDS')
            print("the wheels should be turning")
            """ Makes the robot stop moving when both sensors detect a black line"""
            print("R :"+str(self.right_colour_sensor.reflected_light_intensity))
            print("L :"+str(self.left_colour_sensor.reflected_light_intensity))

            if (self.right_colour_sensor.reflected_light_intensity < 40
                    and self.left_colour_sensor.reflected_light_intensity < 40):
                self.left_wheel.stop()
                self.right_wheel.stop()
                print("Stop robot")
                break

            if self.right_colour_sensor.reflected_light_intensity < 40:
                self.right_wheel.stop()
                print("Right sensor slepp")
                sleep(0.3)

            if self.left_colour_sensor.reflected_light_intensity < 40:
                self.left_wheel.stop()
                print("Left sensor slepp")
                sleep(0.3)

    def follow_until_next_node_p(self):

        while True:
            if self.left_colour_sensor.reflected_light_intensity < 70:
                if self.right_colour_sensor.reflected_light_intensity < 70:

                else:
                    self.left_wheel.run_direct(duty_cycle_sp=self.steering(
                        self.left_colour_sensor.reflected_light_intensity - 30) * 1.5)
            else:
                if self.right_colour_sensor.reflected_light_intensity < 70:
                    self.right_wheel.run_direct(duty_cycle_sp=self.steering(
                        self.right_colour_sensor.reflected_light_intensity - 30) * 1.5)
                else:
                    self.left_wheel.run_direct(duty_cycle_sp=80)
                    self.right_wheel.run_direct(duty_cycle_sp=80)

    @staticmethod
    def steering(value):
        if value < 0:
            return value*8/5+80
        else:
            return -value*8/5+80

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

    def lift(self):
        """Lifts the arm to grab the lid"""
        self.arm.run_to_rel_pos(position_sp=-150, speed_sp=1000)

    def drop(self):
        """Drops the arm to secure the container"""
        self.arm.run_to_rel_pos(position_sp=150)

    def scan(self, sensor):
        """Returns the colour that the color sensor senses"""
        return sensor.color

    def move_to(self, arr):
        """Moves to a given node"""

        for i in arr-1:
            if arr[i].get_n() == arr[i+1].get_name():
                direction = "N"
            elif arr[i].get_e() == arr[i + 1].get_name():
                direction = "E"
            elif arr[i].get_w() == arr[i + 1].get_name():
                direction = "W"
            else:
                direction = "S"
            rotation_degrees = Robot.compass[Robot.rotation] - Robot.compass[direction]
            Robot.rotation = direction
            if rotation_degrees == 270:
                rotation_degrees = -90
            if rotation_degrees == -270:
                rotation_degrees = 90
            if rotation_degrees == 90:
                self.turn('LEFT')
            elif rotation_degrees == -90:
                self.turn('RIGHT')
            self.follow_until_next_node()
