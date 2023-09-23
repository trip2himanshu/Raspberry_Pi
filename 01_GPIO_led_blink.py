# 01_GPIO_led_blink.py
# Python script for Raspberry Pi
# Himanshu Tripathi 

# blink the led connected with gpio pin of pi

import RPi.GPIO as gpio
import time 
import sys

# method to blink the led 
# input parameter: pin (for led connection)
def led_blink(pin):
    # configure the gpio pin 
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.OUT,initial=gpio.LOW)
    led_state = 0
    while True:
        try:
            led_state = not led_state 
            gpio.output(pin,led_state)
            print("LED is on" if led_state else "LED is off")
            time.sleep(1)
        except Exception as e:
            print("Error : ", e)
            break
        except KeyboardInterrupt:
            print("Exit using keyboard interrupt")
            break
    # clean exit 
    gpio.cleanup()
    sys.exit()

# code runs from here 
led_blink(8)