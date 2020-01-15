import ctre


class Drivetrain:
    def __init__(self, front_left: ctre.TalonSRX, front_right: ctre.TalonSRX,
                 back_left: ctre.TalonSRX, back_right: ctre.TalonSRX):
        self.front_left = front_left
        self.front_right = front_right
        self.back_left = back_left
        self.back_right = back_right
        self.speed_left = 0
        self.speed_right = 0

    def setSpeedsFromJoystick(self, x, y, twist):
        speed_left = (-y + (x if x > 0 else 0) + twist)
        speed_right = (-y - (x if x < 0 else 0) - twist)
        # Normalization
        speed_max = max(abs(speed_left), abs(speed_right))
        if speed_max > 1:
            speed_left /= speed_max
            speed_right /= speed_max
        # Set speeds
        self.setSpeeds(speed_left, speed_right)

    def setSpeeds(self, speed_left, speed_right):
        self.speed_left = speed_left
        self.speed_right = speed_right

    def getSpeeds(self):
        return (self.speed_left, self.speed_right)

    def execute(self):
        self.front_left.set(self.speed_left)
        self.front_right.set(self.speed_right)
        self.back_left.set(self.speed_left)
        self.back_right.set(self.speed_right)
