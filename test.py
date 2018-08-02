from src.robot import Robot
from time import sleep
print("Started")
ROBOT = Robot()
print("Running wheels with postive duty cycle")
ROBOT.left_wheel.run_direct(duty_cycle_sp=80)
ROBOT.right_wheel.run_direct(duty_cycle_sp=80)
sleep(10)
print("Running wheels with positive move straight")
ROBOT.stop()
ROBOT.move_straight(100, 100, "FORWARDS")
ROBOT.stop()
print("Stopped")
sleep(2)
print("following")
ROBOT.follow_until_next_node()
sleep(10)
ROBOT.stop()

