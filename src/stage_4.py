from ev3dev.auto import *
import time

def push_ship():
    left_wheel = Motor(OUTPUT_A)
    #right_wheel = Motor(OUTPUT D)

    left_wheel.run_timed(time_sp=3000, speed_sp=500)
    #right_wheel.run_timed(time_sp=3000, speed_sp=500)