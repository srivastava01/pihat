#!/usr/bin/env python3
from sense_hat import SenseHat
sense = SenseHat()
# this script will clear any LEDs left in the 'on' state that a different script may have left
print("clearing LEDs")
sense.clear()
