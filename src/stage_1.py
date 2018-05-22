"""Identify the food colour and picks up the food"""

from ev3dev.auto import *
import time

def run_motor():
    m = Motor(OUTPUT_A)
    m.run_timed(time_sp=3000, speed_sp=500)
