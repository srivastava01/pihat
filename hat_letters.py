#!/usr/bin/env python3 

from sense_hat import SenseHat
sense= SenseHat()
import time 

x = (255,0,0)
y = (255,255,255)
z = (0,0,255)
a = (255,255,0)
b= (255,0,255)

sense.show_letter("H",x,back_colour=a)
time.sleep(1)
sense.show_letter("i",y,back_colour=b)
time.sleep(1)
sense.show_letter("!",z,back_colour=a)
time.sleep(1)
sense.clear()
