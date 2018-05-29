from ev3dev.auto import *
import time

def run_motor(output,time,speed):
    #use as follows: run_motor("A"/"B"/"C"/"D", 1000x where x is no of seconds,
    if output=="A":
        m = Motor(OUTPUT_A)
    if output=="B":
        m = Motor(OUTPUT_B)
    if output=="C":
        m = Motor(OUTPUT_C)
    if output=="D":
        m = Motor(OUTPUT_D)

    m.run_timed(time_sp=time, speed_sp=speed)

def get_colour():
    cs = ColorSensor()
    return cs.raw

