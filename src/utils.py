from ev3dev.auto import *

def run_motor(output,time,speed):
    '''
    Use as follows:
    output = "A"/"B"/"C"/"D"
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

def get_colour():
    cs = ColorSensor()
    return cs.color

def forwards(time, speed):
    run_motor("A", time, speed)
    run_motor("D", time, speed)

def lift():
    lifter = MediumMotor('outB')
    lifter.run_to_rel_pos(-5000, 1000)

def place():
    lifter = MediumMotor('outB')
    lifter.run_to_rel_pos(5000, 1000)