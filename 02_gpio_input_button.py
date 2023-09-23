# 02_gpio_input_button.py
# Python script for Raspberry Pi
# Himanshu Tripathi 

# take input from a push button and toggle 
# the state of led with each button press 

import RPi.GPIO as gpio 
import time 
import sys

# global variables 
led_pin = 8
button_pin = 10
led_state = 0

def gpio_config():
    global led_pin, button_pin 
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    # config led pin 
    gpio.setup(led_pin,gpio.OUT,initial=gpio.LOW)
    # config button pin 
    gpio.setup(button_pin,gpio.IN,pull_up_down=gpio.PUD_UP)


if __name__ == "__main__":
    gpio_config()
    while True:
        try:
            if gpio.input(button_pin) == gpio.LOW:
                led_state = not led_state
                gpio.output(led_pin,led_state)
                print("LED is on" if led_state else "LED is off")
                while gpio.input(button_pin) == gpio.LOW:
                    time.sleep(0.10)
        except Exception as e:
            print("Error : ", e)
            break
        except KeyboardInterrupt:
            print("Exit using keyboard interrupt")
            break
    gpio.cleanup()
    sys.exit()
