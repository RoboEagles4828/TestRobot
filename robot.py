import magicbot 
import wpilib
import json

from components.low.drivetrain import DriveTrain
from components.low.arm import Arm

import logging
logging.basicConfig(level=logging.DEBUG)

class Robot(magicbot.MagicRobot):

    drive: DriveTrain
    arm: Arm

    def createObjects(self):
#         with open("ports.json", "r") as f:
#             self.ports = json.load('''{
#     "drivetrain": {
#         "frontLeft": 6,
#         "frontRight": 7,
#         "backLeft": 8,
#         "backRight": 9
#     },
#     "arm": {
#         "elbowLeft": 0,
#         "elbowRight": 1,
#         "wrist": 3,
#         "roller": 4
#     }
# }''')
        #Lift---------------------------------------------
        self.armLeft = wpilib.Victor(0)
        self.armRight = wpilib.Victor(1)
        self.armWrist = wpilib.Spark(3)
        self.armRoller = wpilib.Spark(4)
        self.hatch = wpilib.DoubleSolenoid(4, 5)

        #DriveTrain---------------------------------------
        self.frontLeft = wpilib.Victor(6)
        self.frontRight = wpilib.Victor(7)
        self.backLeft = wpilib.Victor(8)
        self.backRight = wpilib.Victor(9)

        self.joystick = wpilib.Joystick(0)

        self.printTimer = wpilib.Timer()
        self.printTimer.start()

    def teleopInit(self):
        print("Teleop Started!")
        pass

    def teleopPeriodic(self):
        try:
            #if self.printTimer.hasPeriodPassed(0.5):
            #    self.logger.info("Driving: " + str(self.joystick.getX()) + " " + str(self.joystick.getY()) + " " + str(self.joystick.getTwist()))
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
                self.arm.intake(-0.5)
            elif self.joystick.getRawButton(1):
                self.arm.intake(0.9)
            else:
                self.arm.intake(0)

            if self.joystick.getRawButton(5):
                self.arm.hatchSet(1)
            else:
                self.arm.hatchSet(0)
        except:
            self.onException()

if __name__ == '__main__':
    wpilib.run(Robot)