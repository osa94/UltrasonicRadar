import sys
from time import sleep_us
from ultrasonic_sensor import UltrasonicSensorHCSR04
from servo import ServoSG90

# used pins
TRIGGER_PIN_NR = 0
ECHO_PIN_NR = 1
SERVO_PIN_NR = 2

# device declarations
sensor = UltrasonicSensorHCSR04(0, 1)
servo = ServoSG90(SERVO_PIN_NR)

# constant values
MAX_ANGLE_DEG = 180
MIN_ANGLE_DEG = 0
STEP_ANGLE_DEG = 3
DELAY_US = 30_000

# initialization of initial values
angle = MIN_ANGLE_DEG
reverse = False

# main loop
while True:
    servo.set_angle(angle)
    distance = sensor.get_distance_cm()

    sys.stdout.write(f"{angle},{distance}\r") # send data via usb serial

    # radar movement in the range of 0-180
    if angle >= MAX_ANGLE_DEG:
        angle = MAX_ANGLE_DEG
        reverse=True
    elif angle <= MIN_ANGLE_DEG:
        angle = MIN_ANGLE_DEG
        reverse=False
    else:
        reverse=reverse

    angle = angle - STEP_ANGLE_DEG if reverse else angle + STEP_ANGLE_DEG

    sleep_us(DELAY_US)
