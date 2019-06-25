#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import random
sense = SenseHat()

x = random.randint(0,7)
y = random.randint(0,7)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

print("the x coordinate is"), x, ("this time")

print("the y coordinate is"), y, ("this time")
for i in range(1,5):
    sense.set_pixel(x,y,(r,g,b))
    time.sleep(1)
    sense.set_pixel(x,y,(r,g,b))
sense.clear()


