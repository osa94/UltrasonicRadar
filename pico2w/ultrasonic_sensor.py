from machine import Pin, time_pulse_us
from time import sleep_us

class UltrasonicSensor:

    def __init__(self, trigger_pin_nr, echo_pin_nr):

        self.__trigger_pin = Pin(trigger_pin_nr, mode=Pin.OUT)
        self.__echo_pin = Pin(echo_pin_nr, mode=Pin.IN)

    def get_distance_cm(self):
        self.__trigger_pin.low()
        sleep_us(1)
        self.__trigger_pin.on()
        sleep_us(10)
        self.__trigger_pin.low()
        pulse_us =  time_pulse_us(self.__echo_pin, 1)
        dist = pulse_us * 0.034320 / 2
        return dist