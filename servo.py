#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)

def mover(self):
    servo.start(0)
    servo.ChangeDutyCucle(12)
    time.sleep(0.5)
    servo.ChangeDutyCucle(0)

    time.sleep(2)

    servo.ChangeDutyCucle(2)
    time.sleep(0.5)
    servo.ChangeDutyCucle(0)

    servo.stop()
    GPIO.cleanup()