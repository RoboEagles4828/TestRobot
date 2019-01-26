import wpilib

class lift:
    liftRight: wpilib.Victor
    liftLeft: wpilib.Victor
    def _init_(self):
        self.speed = 0
    def setSpeed(speed):
        self.speed = speed
    def execute(self):
        self.liftRight.set(self.speed)
        self.liftLeft.set(self.speed)
#ports 8 and 9
