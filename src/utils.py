from ev3dev.auto import *

wheel1 = Motor(OUTPUT_A)
wheel2 = Motor(OUTPUT_B)
grabber = Motor(OUTPUT_C)
claw = Motor(OUTPUT_D)

def run_motor(motor,time,speed):
    '''
    Use as follows:
    output = "A"/"B"/"C"/"D"
    time = 1000x where x is no of seconds
    speed = 5y where y is rpm
    '''

    motor.run_timed(time_sp=time, speed_sp=speed)
    #motor.run_to_rel_pos()

def get_colour1():                                  #For a colour sensor in port 1
    cs1 = ColorSensor(address="1")
    return cs1.color


def get_colour2():                                  #For a colour sensor in port 4
    cs2 = ColorSensor(address="4")
    return cs2.color


def forwards(time, speed):
    run_motor(wheel1, time, speed)
    run_motor(wheel2, time, speed)


def lift():
    grabber.run_to_rel_pos(position_sp = -540, speed_sp = 1000)


def place():
    grabber.run_to_rel_pos(position_sp = 540, speed_sp = 1000)
