from machine import Pin, time_pulse_us
from time import sleep_us

class UltrasonicSensorHCSR04:

    HIGH = 1 # high pin state
    LOW = 0 # low pin state

    def __init__(self,
                 trigger_pin_nr: int,
                 echo_pin_nr: int,
                 timeout_us: int =11_000) -> None:
        """
        :param trigger_pin_nr: Trigger pin number (GP)
        :param echo_pin_nr: Echo pin number (GP)
        :param timeout_us: Max time to wait for echo pin (in us)
        """
        self.__trigger_pin = Pin(trigger_pin_nr, mode=Pin.OUT)
        self.__echo_pin = Pin(echo_pin_nr, mode=Pin.IN)
        self.__timeout_us = timeout_us

    def __trigger_signal(self) -> None:
        """
        Method responsible for triggering the signal on the ultrasonic sensor.
        :return: None
        """
        self.__trigger_pin.low()
        sleep_us(1)
        self.__trigger_pin.on()
        sleep_us(10)
        self.__trigger_pin.low()

    def get_distance_cm(self) -> float:
        """
        Method responsible for getting the distance from the ultrasonic sensor.
        :return: Distance calculated in cm
        """
        self.__trigger_signal()
        pulse_us =  time_pulse_us(self.__echo_pin, self.HIGH, self.__timeout_us)
        dist = pulse_us * 0.034320 / 2
        return dist