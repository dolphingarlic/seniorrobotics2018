from ev3dev.auto import *
import time

def run_motor(output,time,speed):
    m = Motor(output)
    m.run_timed(time_sp=time, speed_sp=speed)

def get_colour():
    cs = ColorSensor()
    return cs.raw

