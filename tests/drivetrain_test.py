import random

from components.low.drivetrain import DriveTrain

import logging
logging.basicConfig(level=logging.DEBUG)

def test_standardize(robot):
    drive = DriveTrain()
    print(dir(robot))
    for _ in range(20):
        drive.set(random.random() * 2 - 1, random.random() * 2 - 1, random.random() * 2 - 1)
        assert max([abs(x) for x in drive.debugSpeeds()]) <= 1
