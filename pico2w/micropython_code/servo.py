from machine import PWM, Pin

class ServoSG90:
    MAX_PULSE_WIDTH = 2400_000 # ns
    MIN_PULSE_WIDTH = 400_000 # ns
    MAX_ANGLE = 180 # deg
    WIDTH_PER_ANGLE = (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) / MAX_ANGLE
    FREQUENCY = 50 # Hz

    def __init__(self, servo_pin_nr):
        self.__servo_pin = Pin(servo_pin_nr)
        self.controller = PWM(self.__servo_pin)
        self.controller.freq(self.FREQUENCY)

    def de_init(self):
        self.controller.deinit()

    def set_angle(self, angle):
        width = int(angle * self.WIDTH_PER_ANGLE + self.MIN_PULSE_WIDTH)
        self.controller.duty_ns(width)
