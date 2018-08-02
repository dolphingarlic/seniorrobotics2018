from src.robot import Robot
from time import sleep
print("Started")
ROBOT = Robot()
print("Running wheels with negative duty cycle")
ROBOT.left_wheel.run_direct(duty_cycle_sp=-80)
ROBOT.right_wheel.run_direct(duty_cycle_sp=-80)
sleep(10)
print("Running wheels with positive move straight")
ROBOT.move_straight_time(100, 100, "FORWARDS")
ROBOT.stop()
print("Stopped")
sleep(2)
print("following")
ROBOT.follow_until_next_node()

