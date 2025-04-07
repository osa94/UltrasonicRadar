from machine import PWM, Pin

class ServoSG90:
    MAX_PULSE_WIDTH = 2400_000 # ns
    MIN_PULSE_WIDTH = 400_000 # ns
    MAX_ANGLE = 180 # deg
    WIDTH_PER_ANGLE = (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) / MAX_ANGLE # ns
    FREQUENCY = 50 # Hz

    def __init__(self, servo_pin_nr: int) -> None:
        """
        :param servo_pin_nr: Servo pin number (GP)
        """
        self.__servo_pin = Pin(servo_pin_nr)
        self.controller = PWM(self.__servo_pin)
        self.controller.freq(self.FREQUENCY)

    def de_init(self) -> None:
        """
        Method responsible for de-initialization of servo.
        :return: None
        """
        self.controller.deinit()

    def set_angle(self, angle: int) -> None:
        """
        Method responsible for setting the servo angle (in degree).
        :param angle: Angle in degree
        :return: None
        """
        width = int(angle * self.WIDTH_PER_ANGLE + self.MIN_PULSE_WIDTH)
        self.controller.duty_ns(width)
