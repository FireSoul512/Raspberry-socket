import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

try:
    GPIO.setmode(GPIO.BCM)
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    err = hx.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')
    reading = float(-957009)
    value = float(34)
    reading = hx.get_data_mean()
    print("Nuevo reading ", reading)
    print(value)
    ratio = reading / value
    hx.set_scale_ratio(ratio)
    print(hx.get_weight_mean(20))

finally:
    GPIO.cleanup()