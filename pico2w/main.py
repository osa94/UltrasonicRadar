import sys
from time import sleep_us
from ultrasonic_sensor import UltrasonicSensor

s = UltrasonicSensor(0, 1)
while True:
    distance = s.get_distance_cm()
    sys.stdout.write(f"distance: {distance} cm\r")
    sleep_us(55555)




