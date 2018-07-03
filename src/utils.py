from ev3dev.auto import *

wheel1 = Motor(OUTPUT_A)
wheel2 = Motor(OUTPUT_B)
grabber = Motor(OUTPUT_C)
claw = Motor(OUTPUT_D)

def run_motor(motor,time,speed):
    '''
    Use as follows:
    ouput = "A"/"B"/"C"/"D"
    time = 1000x where x is no of seconds
    speed = 5y where y is rpm
    '''

    motor.run_timed(time_sp=time, speed_sp=speed)

def grab():
    run_motor(grabber, 100, 1000)


def release_grabber():
    run_motor(grabber, 1000, -1000)



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
    lifter = MediumMotor('outB')
    lifter.run_to_rel_pos(-5000, 1000)

def place():
    lifter = MediumMotor('outB')
    lifter.run_to_rel_pos(5000, 1000)