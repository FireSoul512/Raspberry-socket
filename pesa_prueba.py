#!/usr/bin/env python3
import pickle
import os

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=5, pd_sck_pin=6)

if os.path.isfile(swap_file_name):
    with open(swap_file_name, 'rb') as swap_file:
        hx = pickle.load(swap_file)
    
    print(hx.get_weight_mean(20), 'g')
    
else:
    print("No hay datos cargados, porfavor ejecutar la app para guardarlos ;v")

print('Bye :)')

GPIO.cleanup()