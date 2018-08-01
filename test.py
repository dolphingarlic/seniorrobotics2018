from src.robot import Robot
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
'''
'''
for i in range(50):
    print("Right: "+str(ROBOT.right_colour_sensor.reflected_light_intensity))
    print("Left: "+str(ROBOT.left_colour_sensor.reflected_light_intensity))
    sleep(0.5)
