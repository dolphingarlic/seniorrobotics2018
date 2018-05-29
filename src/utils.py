from ev3dev.auto import *
import time

def run_motor(output, time, speed):
    if output == "A":
        m = Motor(OUTPUT_A)
    elif output == "B":
        m = Motor(OUTPUT_B)
    elif output == "C":
        m = Motor(OUTPUT_C)
    elif output == "D":
        m = Motor(OUTPUT_D)

    m.run_timed(time_sp=time, speed_sp=speed)

def get_colour():
    cs = ColorSensor()
    return cs.value;

def forwards():
    m_a = Motor(OUTPUT_A)
    m_d = Motor(OUTPUT_D)

    m_a.run_direct(time = 1000000, speed = 500)
    m_d.run_direct(time = 1000000, speed = 500)