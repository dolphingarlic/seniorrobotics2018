"""A simple Robot class for the EV3 robots"""

from ev3dev.auto import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, ColorSensor
from time import time, sleep
from src.map_nodes import *


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
    rotation_angle = 180
    compass = {'N': 0, 'E': 90, 'S': 180, 'W': -90}
    compass_degrees = {0 :'N', 90 :'E', 180 : 'S', 270 : 'W'}

    COLORS = {2: 'BLUE', 3: 'GREEN', 4: 'YELLOW', 5: 'RED'}
    INTENSITY_THRESHOLD = 40
    PROPORTIONAL_THRESHOLD = 24       # TODO: Calculate a more specific proportional threshold
    BACK_THRESHOLD = 51
    FRONT_THRESHOLD = 51

    def __init__(self):
        self.grabber = Motor(OUTPUT_C)
        self.arm = Motor(OUTPUT_B)
        self.left_colour_sensor = ColorSensor(address='3')
        self.right_colour_sensor = ColorSensor(address='4')
        self.inner_colour_sensor = ColorSensor(address='1')
        self.outer_colour_sensor = ColorSensor(address='2')
        self.left_wheel = Motor(OUTPUT_A)
        self.right_wheel = Motor(OUTPUT_D)
        self.stop_action = "coast"

        self.current_node = A1

    def move_straight_degrees(self, degrees, speed, direction):
        """Moves the robot straight for the degrees specified"""
        """Direction: 1 - Forwards, -1 - Backwards"""

        self.left_wheel.run_to_rel_pos(position_sp=-degrees, speed_sp=direction*speed)
        self.right_wheel.run_to_rel_pos(position_sp=-degrees, speed_sp=direction*speed)

    def move_straight(self, move_time, speed, direction):
        """Moves the robot straight for a given time"""
        """Direction -> 1 = forwards -> -1 = backwards"""
        self.left_wheel.run_timed(time_sp=move_time, speed_sp=direction*speed)
        self.right_wheel.run_timed(time_sp=move_time, speed_sp=direction*speed)

    def stop(self):
        self.right_wheel.stop()
        self.left_wheel.stop()

    def follow_black_line(self, move_time):
        """Makes the robot follow the black line for a period of time"""
        timeout = time() + move_time
        self.move_straight(move_time, 500, 1)

        while time() < timeout:
            if self.front_colour_sensor.reflected_light_intensity < Robot.INTENSITY_THRESHOLD:
                self.right_wheel.stop()
                sleep(0.1)
                self.move_straight(timeout - time(), 500, 'FORWARDS')
            if self.left_colour_sensor.reflected_light_intensity < Robot.INTENSITY_THRESHOLD:
                self.left_wheel.stop()
                sleep(0.1)
                self.move_straight(timeout - time(), 500, 1)

        print('Success!')

    def follow_until_next_node(self):
        """Makes the robot follow the black line until a node"""
        time_start = time()
        speed = 60
        self.left_wheel.run_direct(duty_cycle_sp=speed)
        self.right_wheel.run_direct(duty_cycle_sp=speed)
        x = 1
        while True:
            print(x)
            x += 1
            print("Threshold: "+str(self.INTENSITY_THRESHOLD))
            print("Left: " + str(self.left_colour_sensor.reflected_light_intensity))
            print("Right: " + str(self.right_colour_sensor.reflected_light_intensity))

            print(left)
            if self.left_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD:
                if self.right_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD \
                        and time_start > time()+50:
                    print("(1)stop")
                else:
                    self.right_wheel.duty_cycle_sp = speed
                    self.left_wheel.duty_cycle_sp = self.steering((
                        self.left_colour_sensor.reflected_light_intensity))
                    print("(2)Left Intensity: "+str(self.left_colour_sensor.reflected_light_intensity)+"  Right Speed: "+str(
                        self.steering(
                            self.left_colour_sensor.reflected_light_intensity)))
            else:
                if self.right_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD:
                    self.left_wheel.duty_cycle_sp = speed
                    self.right_wheel.duty_cycle_sp = self.steering(
                        self.right_colour_sensor.reflected_light_intensity)
                    print("(3)Right Intensity: "+str(self.right_colour_sensor.reflected_light_intensity)
                          + "   Left Speed: "+str(self.steering(
                                self.right_colour_sensor.reflected_light_intensity)))
                else:
                    self.right_wheel.duty_cycle_sp = speed
                    self.left_wheel.duty_cycle_sp = speed
                    print("(4)Straight")

    def follow_black_line_degrees(self, degrees, speed, direction):
        """Makes the robot follow the black line until a distance has been travelled"""
        degrees_moved = 0
        while True:  # TODO: Is -60 a good modifier? Test on Thursday
            if degrees_moved >= degrees:
                self.stop()
                break
            if self.back_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD:
                if self.front_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD:
                    print("Node?")
                else:
                    self.right_wheel.run_to_rel_pos(position_sp=-self.steering(
                        self.back_colour_sensor.reflected_light_intensity - 60), speed_sp=speed * direction)
                    degrees_moved += self.back_colour_sensor.reflected_light_intensity - 60
                    print("Left: " + str(self.steering(
                        self.back_colour_sensor.reflected_light_intensity - 60)))
            else:
                if self.front_colour_sensor.reflected_light_intensity < self.PROPORTIONAL_THRESHOLD:
                    self.left_wheel.run_to_rel_pos(position_sp=-self.steering(
                        self.front_colour_sensor.reflected_light_intensity - 60), speed_sp=speed * direction)
                    degrees_moved += self.front_colour_sensor.reflected_light_intensity - 60
                    print("Right: " + self.steering(
                        self.front_colour_sensor.reflected_light_intensity - 60))
                else:
                    self.move_straight_degrees(30, speed, direction)
                    print("Straight: 30")
                    degrees_moved += 30

    def reverse_till_black_line(self, direction, speed):
        self.right_wheel.run_direct(speed_sp=direction*speed)
        self.left_wheel.run_direct(speed_sp=direction*speed)
        if (self.front_colour_sensor.reflected_light_intensity < self.INTENSITY_THRESHOLD
                and self.back_colour_sensor.reflected_light_intensity < self.INTENSITY_THRESHOLD):
            self.stop()

    def __change_direction_(self, angle):
        self.rotation_angle += angle
        if self.rotation_angle >= 360:
            self.rotation_angle -= 360
        if self.rotation_angle < 0:
            self.rotation_angle += 360
        self.rotation = self.compass_degrees[self.rotation_angle]

    def turn(self, direction):
        """Turns the robot 90 degrees in a given direction"""
        if direction.upper() == 'LEFT':
            self.left_wheel.run_to_rel_pos(position_sp=240, speed_sp=300)
            self.right_wheel.run_to_rel_pos(position_sp=-240, speed_sp=300)
            self.__change_direction_(-90)
        elif direction.upper() == 'RIGHT':
            self.left_wheel.run_to_rel_pos(position_sp=-240, speed_sp=300)
            self.right_wheel.run_to_rel_pos(position_sp=240, speed_sp=300)
            self.__change_direction_(90)
        elif direction.upper() == 'AROUND':  # 180 degrees around fantastical
            self.left_wheel.run_to_rel_pos(position_sp=-480, speed_sp=300)
            self.right_wheel.run_to_rel_pos(position_sp=480, speed_sp=300)
            self.__change_direction_(180)

    def grab(self):
        """Makes the grabber grab the food brick"""
        self.grabber.run_to_rel_pos(position_sp=-540, speed_sp=1000)

    def release(self):
        """Makes the grabber release the food brick"""
        self.grabber.run_to_rel_pos(position_sp=540, speed_sp=1000)

    def lift(self):
        """Lifts the arm to grab the lid"""
        self.arm.run_to_rel_pos(position_sp=-120, speed_sp=500)

    def drop(self):
        """Drops the arm to secure the container"""
        self.arm.run_to_rel_pos(position_sp=120, speed_sp=500)

    def scan(self, sensor):
        """Returns the colour that the color sensor senses"""
        if sensor.upper() == "RIGHT":
            return self.front_colour_sensor.color
        if sensor.upper() == "LEFT":
            return self.back_colour_sensor.color
        if sensor.upper() == "INNER":
            return self.inner_colour_sensor.color
        if sensor.upper() == "OUTER":
            return self.outer_colour_sensor.color

    @staticmethod
    def steering(value):
        return value / 28 * 60

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
            if rotation_degrees == 270:
                rotation_degrees = -90
            if rotation_degrees == -270:
                rotation_degrees = 90
            if rotation_degrees == 90:
                self.turn('LEFT')
            elif rotation_degrees == -90:
                self.turn('RIGHT')
            self.follow_until_next_node()
            self.current_node = arr[i+1]

    def move_to_adjacent(self, next_node):
        """Moves one node"""
        if self.current_node.get_n() == next_node.get_name():
            direction = "N"
        elif self.current_node.get_e() == next_node.get_name():
            direction = "E"
        elif self.current_node.get_w() == next_node.get_name():
            direction = "W"
        else:
            direction = "S"
        rotation_degrees = Robot.compass[Robot.rotation] - Robot.compass[direction]
        if rotation_degrees == 270:
            rotation_degrees = -90
        if rotation_degrees == -270:
            rotation_degrees = 90
        if rotation_degrees == 90:
            self.turn('LEFT')
        elif rotation_degrees == -90:
            self.turn('RIGHT')
        self.follow_until_next_node()
        self.current_node = next_node

    def take_lid_and_place_box(self):
        self.lift()
        self.arm.wait_until_not_moving()
        self.move_straight_degrees(235, 300, 1)
        self.left_wheel.wait_until_not_moving()
        sleep(2)
        self.move_straight_degrees(-235, 300, 1)

    def deposit_food_and_cover(self):
        self.move_straight_degrees(235, 300, 1)
        self.left_wheel.wait_until_not_moving()
        self.release()
        self.move_straight_degrees(200, 300, -1)  # backwards
        self.left_wheel.wait_until_not_moving()
        self.drop()