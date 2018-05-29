from ev3dev.auto import *
import asyncio
from concurrent.futures import ProcessPoolExecutor

def run_motor(output,time,speed):
    # use as follows:
    # ouput = "A"/"B"/"C"/"D"
    # time = 1000x where x is no of seconds
    # speed = 0.5y where y is rpm)
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
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    m_1 = asyncio.ensure_future(loop.run_in_executor(executor, run_motor(OUTPUT_A, 1000, 500)))
    m_2 = asyncio.ensure_future(loop.run_in_executor(executor, run_motor(OUTPUT_D, 1000, 500)))

    loop.run_forever()