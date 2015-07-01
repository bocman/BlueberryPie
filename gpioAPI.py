#!/usr/bin/python

import RPi.GPIO as GPIO  # Import GPIO library
import time


def blink(numTimes, speed):
    GPIO.setup(16, GPIO.OUT)
    for i in range(0, numTimes):
        print "Iteration " + str(i+1)
        GPIO.output(16, False)
        time.sleep(1)
        GPIO.output(16, True)
        time.sleep(1)
    

#blink(8, 3)

class RaspberryGPIO(object):

    min_pin = 1
    max_pin = 27
    statuses = {key: False for key in range(1, 28)}

    def __init__(self, model=None):
        GPIO.setmode(GPIO.BOARD)
        

    def activate(self, pin):
        if pin < self.min_pin or pin > self.max_pin:
            raise ValueError('Pin number is not in valid range')

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

        self.statuses[pin] = False
        GPIO.output(pin, False)
        time.sleep(3)
        GPIO.output(pin, True)
        GPIO.cleanup()

    def deactivate(self, pin):
        if pin < self.min_pin or pin > self.max_pin:
            raise ValueError('Pin number is not in valid range')
        self.statuses[pin] = True
        GPIO.output(pin, False)

    def get_status(self):
        return self.statuses

    def blink(self, pin, repeat, speed):
        GPIO.setup(pin, GPIO.OUT)
        for i in range(0, repeat):
            GPIO.output(pin, False)
            time.sleep(speed)
            GPIO.output(pin, True)
            time.sleep(speed)
        GPIO.cleanup()


if __name__ == '__main__':

    raspberry = RaspberryGPIO()
    raspberry.blink(7, 5, 1)

