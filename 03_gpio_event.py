# 03_gpio_event.py
# Python script for Raspberry Pi
# Himanshu Tripathi

# push button interfacing using interrupts (event handling)
# toggle the led state with each press of button

import RPi.GPIO as gpio
import sys

# global variables
led_pin = 8
button_pin = 10
led_state = 0
button_state = True


# method to configure the gpio
def gpio_config():
    global led_pin, button_pin
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    # config led pin
    gpio.setup(led_pin, gpio.OUT, initial=gpio.LOW)
    # config button pin
    gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)


# callback function for button event (ISR)
def button_handler(button):
    global button_state
    # setup a flag
    button_state = False


if __name__ == "__main__":
    gpio_config()
    # add event with the button pin
    # button pin is configured with input pull up
    # button pin value goes low when it is pressed
    gpio.add_event_detect(button_pin, gpio.FALLING, callback=button_handler)
    while True:
        try:
            # act as per the flag and reset it
            if button_state == False:
                led_state = not led_state
                gpio.output(led_pin, led_state)
                print("LED is on" if led_state else "LED is off")
                button_state = True
        except Exception as e:
            print("Error : ", e)
            break
        except KeyboardInterrupt:
            print("Exit using keyboard interrupt")
            break
    gpio.cleanup()
    sys.exit()
