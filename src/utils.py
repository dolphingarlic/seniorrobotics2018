from ev3dev.auto import *

def run_motor(output,time,speed):
    '''
    Use as follows:
    ouput = "A"/"B"/"C"/"D"
    time = 1000x where x is no of seconds
    speed = 5y where y is rpm
    '''
    if output=="A":
        m = Motor(OUTPUT_A)
    if output=="B":
        m = Motor(OUTPUT_B)
    if output=="C":
        m = Motor(OUTPUT_C)
    if output=="D":
        m = Motor(OUTPUT_D)

    m.run_timed(time_sp=time, speed_sp=speed)

def get_colour1():
    cs1 = ColorSensor(address="1")
    return cs1.color

def get_colour2():
    cs2 = ColorSensor(address="4")
    return cs2.color


def forwards(time, speed):
    run_motor("A", time, speed)
    run_motor("D", time, speed)

def lift():
    lifter = Motor(OUTPUT_B)
    lifter.run_to_rel_position(-5000, 1000)
def place():
    lifter = Motor(OUTPUT_B)
    lifter.run_to_rel_position(5000, 1000)