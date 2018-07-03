#!/usr/bin/env python3

from ev3dev.ev3 import *
import src.stage_1 as stage_1
import src.utils as utils
#initializes motor objects, change outputs based on ports blugged into
utils.grab()
#utils.release_grabber()

