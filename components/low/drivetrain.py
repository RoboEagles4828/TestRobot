"""Drivetrain module"""
import ctre


class Drivetrain:
    """Drivetrain class"""
    def __init__(self, left_0: ctre.WPI_TalonSRX, left_1: ctre.WPI_TalonSRX,
                 right_0: ctre.WPI_TalonSRX, right_1: ctre.WPI_TalonSRX):
        self.left_0 = left_0
        self.left_1 = left_1
        self.right_0 = right_0
        self.right_1 = right_1
        self.speed_left = 0
        self.speed_right = 0

    def set_speeds(self, speed_left: float, speed_right: float) -> None:
        """
        Sets the left and right speeds

        :param speed_left: The left speed
        :param speed_right: The right speed
        """
        self.speed_left = speed_left
        self.speed_right = speed_right

    def get_speeds(self) -> tuple:
        """
        Gets the left and right speeds

        :returns: A tuple containing the left speed and the right speed
        """
        return (self.speed_left, self.speed_right)

    def set_speeds_joystick(self, x: float, y: float, twist: float) -> None:
        """
        Sets the left and right speeds from joystick inputs

        :param x: The x value of the joystick
        :param y: The y value of the joystick
        :param twist: The twist value of the joystick
        """
        speed_left = (y + (x if x > 0 else 0) + twist)
        speed_right = (y - (x if x < 0 else 0) - twist)
        # Normalization
        speed_max = max(abs(speed_left), abs(speed_right))
        if speed_max > 1:
            speed_left /= speed_max
            speed_right /= speed_max
        # Set speeds
        self.set_speeds(speed_left, speed_right)

    def execute(self):
        self.left_0.set(self.speed_left)
        self.left_1.set(self.speed_left)
        self.right_0.set(self.speed_right)
        self.right_1.set(self.speed_right)
