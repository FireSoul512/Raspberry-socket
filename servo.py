#!/usr/bin/env python3


class SERVO:

    def start(self):
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11,GPIO.OUT)
        servo = GPIO.PWM(11,50)

        servo.start(0)
        servo.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)

        servo.stop()
        GPIO.cleanup()

    def mover(self):

        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11,GPIO.OUT)
        servo = GPIO.PWM(11,50)

        servo.start(0)
        servo.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)

        time.sleep(2)

        servo.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)

        servo.stop()
        GPIO.cleanup()