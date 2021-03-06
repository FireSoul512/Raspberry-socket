#!/usr/bin/env python3
import pickle
import os

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

GPIO.setmode(GPIO.BCM)
hx = HX711(dout_pin=5, pd_sck_pin=6)

swap_file_name = 'swap_file.swp'
if os.path.isfile(swap_file_name):
    with open(swap_file_name, 'rb') as swap_file:
        hx = pickle.load(swap_file)
    
    peso = int(hx.get_weight_mean(20))
    print(peso,"g")
    
else:
    print("No hay datos cargados, porfavor ejecutar la app para guardarlos ;v")

GPIO.cleanup()