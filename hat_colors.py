#!/usr/bin/env python3 

from sense_hat import SenseHat
sense = SenseHat()

x = (255,255,0)
y = (0,0,255)

speed = 0.5

message = "Hello World!"

sense.show_message(message, speed, text_colour= x, back_colour=y)

sense.clear()
