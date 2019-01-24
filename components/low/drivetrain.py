import wpilib

class DriveTrain:
    frontLeft: wpilib.Victor
    frontRight: wpilib.Victor
    backLeft: wpilib.Victor
    backRight: wpilib.Victor

    def __init__(self):
        print("DriveTrain created")
        self.speeds = []

    def set(self, x, y, twist):
        speeds = []
        speeds.append((y - x + twist)*1.0)
        speeds.append((y + x - twist)*1.0)
        speeds.append((y + x + twist)*1.0)
        speeds.append((y - x - twist)*1.0)
        print(speeds)
        if max([abs(x) for x in speeds]) > 1: 
            speeds = [(max([abs(y) for y in speeds]) / x) for x in speeds]
        print(speeds)

        self.speeds = speeds

    def debugSpeeds(self):
        return self.speeds

    def execute(self):
        self.frontLeft.set(self.speeds[0])
        self.frontRight.set(self.speeds[1])
        self.backLeft.set(self.speeds[2])
        self.backRight.set(self.speeds[3])

        self.enabled = False