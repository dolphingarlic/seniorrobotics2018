from src.robot import Robot
from time import sleep
ROBOT = Robot()
print("Started")
ROBOT.follow_until_next_node()
sleep(10)
ROBOT.stop()
print("Stopped")
