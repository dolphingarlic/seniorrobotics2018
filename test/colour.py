from src.robot import Robot
from time import sleep
ROBOT = Robot()
for i in range(50):
    print("Front: "+str(ROBOT.front_colour_sensor.reflected_light_intensity))
    print("Back: "+str(ROBOT.back_colour_sensor.reflected_light_intensity))
    sleep(0.2)
