import magicbot 
import wpilib
import json

from components.low.drivetrain import DriveTrain
from components.low.lift import Lift

import logging
logging.basicConfig(level=logging.DEBUG)

class Robot(magicbot.MagicRobot):

    drive: DriveTrain
    arm: Arm

    def createObjects(self):
        with open("ports.json", "r") as f:
            self.ports = json.load(f)
        #Lift---------------------------------------------
        self.wristSpeed = 0
        self.speed = 0
        self.armLeft = wpilib.Victor(self.ports["arm"]["left"])
        self.armRight = wpilib.Victor(self.ports["arm"]["right"])

        #DriveTrain---------------------------------------
        self.frontLeft = wpilib.Victor(self.ports["drivetrain"]["frontLeft"])
        self.frontRight = wpilib.Victor(self.ports["drivetrain"]["frontRight"])
        self.backLeft = wpilib.Victor(self.ports["drivetrain"]["backLeft"])
        self.backRight = wpilib.Victor(self.ports["drivetrain"]["backRight"])

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
            if joystick.getRawButton(9):
                arm.setSpeed(0.1)
            if joystick.getRawButton(11):
                arm.setSpeed(-0.1)
            if joystick.getRawButton(12):
                arm.setSpeed(0)
            if joystick.getRawButton(3):
                arm.set
                
        except:
            self.onException()

if __name__ == '__main__':
    wpilib.run(Robot)