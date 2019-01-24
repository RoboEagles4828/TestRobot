import random

from components.low.drivetrain import DriveTrain

def test_standardize(robot):
    drive = DriveTrain()
    for _ in range(20):
        drive.set(random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1))
        assert max([abs(x) for x in drive.debugSpeeds()]) <= 1
