#!/usr/bin/env python3

from sense_hat import SenseHat
import time
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)

pixels = [
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
]

sense.set_pixels(pixels)
time.sleep(2)

pixel = [
    b,b,b,b,w,w,w,w,
    b,b,b,b,w,w,w,w,
    b,b,b,b,w,w,w,w,
    b,w,w,b,w,w,w,w,
    b,w,w,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
    b,b,b,b,r,r,r,r,
]
sense.set_pixels(pixel)

