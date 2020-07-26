#!/usr/bin/env python3

class PESO:
    def obtener(self):
        import pickle
        import os

        import RPi.GPIO as GPIO  # import GPIO
        from hx711 import HX711  # import the class HX711
        GPIO.setmode(GPIO.BCM)
        hx = HX711(dout_pin=5, pd_sck_pin=6)

        swap_file_name = 'swap_file.swp'
        try:
            if os.path.isfile(swap_file_name):
                with open(swap_file_name, 'rb') as swap_file:
                    hx = pickle.load(swap_file)
                peso = int(hx.get_weight_mean(20))
                GPIO.cleanup()
                return peso
                
            else:
                GPIO.cleanup()
                XD = int(-500)
                return XD
        except error:
            GPIO.cleanup()
            XD = int(-50)
            return XD