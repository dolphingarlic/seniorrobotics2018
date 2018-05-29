#!/usr/bin/env python3

from ev3dev.ev3 import *
import src.stage_1 as stage_1
import src.utils as utils

motor_a = Motor(OUTPUT_A)

utils.run_motor("A", 1000, 1000)
utils.run_motor("D", 1000, 1000)
motor_a.wait_while('running')

utils.lift()
