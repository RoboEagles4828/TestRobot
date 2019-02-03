import wpilib
import ctre

class Arm:

    arm_left: ctre.WPI_TalonSRX
    arm_right: ctre.WPI_TalonSRX
    wrist: ctre.WPI_TalonSRX
    intake: ctre.WPI_TalonSRX
    hatch: wpilib.DoubleSolenoid

    def __init__(self):
        self.speed = 0
        self.wrist_speed = 0
        self.intake_speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setWristSpeed(self, speed):
        self.wrist_speed = speed

    def setIntakeSpeed(self, speed):
        self.intake_speed = speed

    def setHatch(self, x):
        if x:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.hatch.set(wpilib.DoubleSolenoid.Value.kReverse)

    def getEncVal(self):
        return self.arm_left.FeedbackDevice.CTRE_MagEncoder_Absolute

    def execute(self):
        self.arm_left.set(self.speed)
        self.arm_right.set(self.speed)
        self.wrist.set(self.wrist_speed)
        self.intake.set(self.intake_speed)
