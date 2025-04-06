import sys
from time import sleep_us
from ultrasonic_sensor import UltrasonicSensor
from servo import ServoSG90

sensor = UltrasonicSensor(0, 1)
servo = ServoSG90(2)
angle = 0
reverse = False
while True:

    servo.set_angle(angle)
    distance = sensor.get_distance_cm()

    sys.stdout.write(f"{angle},{distance}\r")

    #sleep_ms(1)
    if angle == 180:
        reverse=True
    elif angle == 0:
        reverse=False
    else:
        reverse=reverse

    if reverse:
        angle -= 2
    else:
        angle += 2
    # sleep_us(55555)
    sleep_us(30000)
