import wpilib
import ctre

class Arm:
    armRight: ctre.WPI_TalonSRX
    armLeft: wpilib.Victor
    armWrist: ctre.WPI_TalonSRX
    armRoller: wpilib.Spark
    hatch: wpilib.DoubleSolenoid

    def __init__(self):
        self.speed = 0
        self.wristSpeed = 0
        self.intakeSpeed = 0
    def setSpeed(self, speed):
        self.speed = speed
    def armWristSpeed(self,speed):
        self.wristSpeed = speed
    def intake(self, speed):
        self.intakeSpeed = speed
        
    def hatchSet(self, val):
        if val == 1:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kReverse)
                
    
    def execute(self):
        self.armRight.set(self.speed)
        self.armLeft.set(self.speed)
        self.armWrist.set(self.wristSpeed)
        self.armRoller.set(self.intakeSpeed)
#ports 8 and 9
