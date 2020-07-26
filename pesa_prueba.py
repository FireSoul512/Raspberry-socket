import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

try:
    GPIO.setmode(GPIO.BCM)
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    err = hx.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')
    reading = float(-3318)
    value = float(35)
    print("reading ",reading)
    print("Value: ",value)
    ratio = reading / value
    hx.set_scale_ratio(ratio)
    print(hx.get_weight_mean(20))

finally:
    GPIO.cleanup()