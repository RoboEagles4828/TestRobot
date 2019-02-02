import wpilib

class DriveTrain:

    front_left: wpilib.Spark
    front_right: wpilib.Spark
    back_left: wpilib.Spark
    back_right: wpilib.Spark

    def __init__(self):
        print("DriveTrain created")
        self.speeds = [0, 0, 0, 0]

    def set(self, x, y, twist):
        speeds = []

        speeds.append((y + (x if x > 0 else 0) + twist))
        speeds.append((y - (x if x < 0 else 0) - twist))
        speeds.append((y + (x if x > 0 else 0) + twist))
        speeds.append((y - (x if x < 0 else 0) - twist))

        abs_speeds = [abs(x) for x in speeds]
        if max(abs_speeds) > 1:
            speeds = [x / max(abs_speeds) for x in speeds]

        self.speeds = speeds

    def setSpeeds(self, a, b, c, d):
        self.speeds = [a, b, c, d]

    def getSpeeds(self):
        return self.speeds

    def execute(self):
        self.front_left.set(self.speeds[0])
        self.front_right.set(self.speeds[1])
        self.back_left.set(self.speeds[2])
        self.back_right.set(self.speeds[3])
