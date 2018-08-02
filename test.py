from src.robot import Robot
from time import sleep
ROBOT = Robot()

print("Started")
'''
ROBOT.follow_until_next_node()
sleep(10)
ROBOT.stop()
print("Stopped")
'''
'''
for i in range(40):
    print("L:"+str(ROBOT.left_colour_sensor.reflected_light_intensity))
    print("R:"+str(ROBOT.right_colour_sensor.reflected_light_intensity))
'''
'''
print("Left: "+str(ROBOT.left_colour_sensor.reflected_light_intensity))
print("Right: "+str(ROBOT.right_colour_sensor.reflected_light_intensity))
print("Inner: "+str(ROBOT.inner_colour_sensor.reflected_light_intensity))
print("Outer: "+str(ROBOT.outer_colour_sensor.reflected_light_intensity))
'''

for i in range(1):
    print("Front: " + str(ROBOT.front_colour_sensor.reflected_light_intensity))
    print("Back: " + str(ROBOT.back_colour_sensor.reflected_light_intensity))
    sleep(0.2)
