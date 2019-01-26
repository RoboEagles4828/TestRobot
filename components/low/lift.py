import wpilib

class Lift:
    liftRight: wpilib.Victor
    liftLeft: wpilib.Victor
    def __init__(self):
        self.speed = 0
    def setSpeed(self, speed):
        self.speed = speed
    def execute(self):
        self.liftRight.set(self.speed)
        self.liftLeft.set(-self.speed)
    
#ports 8 and 9
