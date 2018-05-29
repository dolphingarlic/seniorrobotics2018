from ev3dev.auto import *
import time

def run_motor(output,time,speed):
    # use as follows:
    # ouput = "A"/"B"/"C"/"D"
    # time = 1000x where x is no of seconds
    # speed = 5y where y is rpm)
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

def forwards():
    m_1 = Motor(OUTPUT_A)
    m_2 = Motor(OUTPUT_D)

    m_1.run_direct(time = 1000000, speed = 500)
    m_2.run_direct(time = 1000000, speed = 500)