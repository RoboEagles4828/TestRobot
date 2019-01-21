import wpilib

class DriveTrain:
    frontLeft: wpilib.VictorSP
    frontRight: wpilib.VictorSP
    backLeft: wpilib.VictorSP
    backRight: wpilib.VictorSP
    speeds: {0,0,0,0}

    def _init_(self):
        print("DriveTrain created")

    def set(self, x, y, twist):
        self.speeds[0] = (y - x + twist) / 3
        self.speeds[1] = (y + x - twist) / 3
        self.speeds[2] = (y + x + twist) / 3
        self.speeds[3] = (y - x - twist) / 3

    def execute(self):
        self.frontLeft.set(self.speeds[0])
        self.frontRight.set(self.speeds[1])
        self.backLeft.set(self.speeds[2])
        self.backRight.set(self.speeds[3])

        self.enabled = False