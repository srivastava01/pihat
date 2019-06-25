#!/usr/bin/env python3

from sense_hat import SenseHat
import time
sense = SenseHat()
sense.set_pixel(4,2,(0,0,255))
sense.set_pixel(3,4,(0,255,0))
sense.set_pixel(1,5,(255,0,0))
sense.set_pixel(2,6,(255,0,0))
sense.set_pixel(3,6,(255,0,0))
sense.set_pixel(4,6,(255,0,0))
sense.set_pixel(5,5,(255,0,0))
sense.set_pixel(2,2,(0,0,255))
time.sleep(0.5)
sense.set_pixel(2,2,(0,0,0))
time.sleep(0.5)
sense.set_pixel(2,2,(0,0,255))
time.sleep(1)
sense.clear(1)
