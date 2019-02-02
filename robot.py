import magicbot 
import wpilib, ctre
from wpilib.shuffleboard import Shuffleboard
import json, os

from components.low.drivetrain import DriveTrain
from components.low.arm import Arm

import logging
logging.basicConfig(level=logging.DEBUG)
class Robot(magicbot.MagicRobot):

    drive: DriveTrain
    arm: Arm

    def createObjects(self):
        with open("../ports.json" if os.getcwd()[-5:-1] == "test" else "ports.json") as f:
            self.ports = json.load(f)
        # Lift
        armPorts = self.ports["arm"]
        self.armLeft = wpilib.Victor(armPorts["elbowLeft"])
        self.armRight = ctre.WPI_TalonSRX(armPorts["elbowRight"])
        self.armWrist = ctre.WPI_TalonSRX(armPorts["wrist"])
        self.armRoller = wpilib.Spark(armPorts["roller"])
        self.hatch = wpilib.DoubleSolenoid(armPorts["hatchA"], armPorts["hatchB"])

        # DriveTrain 
        drivePorts = self.ports["drivetrain"]
        self.frontLeft = wpilib.Victor(drivePorts["frontLeft"])
        self.frontRight = wpilib.Victor(drivePorts["frontRight"])
        self.backLeft = wpilib.Victor(drivePorts["backLeft"])
        self.backRight = wpilib.Victor(drivePorts["backRight"])

        self.joystick = wpilib.Joystick(0)

        self.printTimer = wpilib.Timer()
        self.printTimer.start()
        wpilib.CameraServer.launch()
        
        self.logger = logging.getLogger("Robot")
        self.testTab = Shuffleboard.getTab("Test")


    def teleopInit(self):
        print("Teleop Started!")
        
        pass

    def teleopPeriodic(self):
        try:
            self.drive.set(self.joystick.getX(), self.joystick.getY(), self.joystick.getTwist())
            if self.joystick.getRawButton(9):
                self.arm.setSpeed(0.3)
            elif self.joystick.getRawButton(11):
                self.arm.setSpeed(-0.3)
            else:
                self.arm.setSpeed(0)
            if self.joystick.getRawButton(3):
                self.arm.armWristSpeed(.3)
            else:
                self.arm.armWristSpeed(0)
                
            if self.joystick.getRawButton(2):
                self.arm.intake(-1)
            elif self.joystick.getRawButton(1):
                self.arm.intake(1)
            else:
                self.arm.intake(0)

            if self.joystick.getRawButton(5):
                self.arm.hatchSet(1)
            else:
                self.arm.hatchSet(0)
        except:
            self.onException()

    def testInit(self):
        print("Starting Test")
        self.testSpd = (
            self.testTab
            .add(title="Speed", value=0.1)
            .withWidget("Number Slider")
        )

    def testPeriodic(self):
        self.armRight.set(self.testSpd.getDouble(1.0))
        self.armWrist.set(self.testSpd.getDouble(1.0))

if __name__ == '__main__':
    wpilib.run(Robot)