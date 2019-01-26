import wpilib

class Arm:
    armRight: wpilib.Victor
    armLeft: wpilib.Victor
    armWrist: wpilib.Spark
    def __init__(self):
        self.speed = 0
        self.armSpeed = 0
    def setSpeed(self, speed):
        self.speed = speed
    def armWristSpeed(self,speed)
        self.wristSpeed = 0
    def execute(self):
        self.liftRight.set(self.speed)
        self.liftLeft.set(self.speed)
        self.armPivot.set(self.armSpeed)
    
#ports 8 and 9
