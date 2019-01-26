import magicbot 
import wpilib
import json

from components.low.drivetrain import DriveTrain
from components.low.lift import Lift

import logging
logging.basicConfig(level=logging.DEBUG)

class Robot(magicbot.MagicRobot):

    drive: DriveTrain
    lift: Lift

    def createObjects(self):
        with open("../ports.json") as f:
            self.ports = json.load(f)

        #Lift---------------------------------------------
        self.speed = 0
        self.liftLeft = wpilib.Victor(self.ports["arm"]["left"])
        self.liftRight = wpilib.Victor(self.ports["arm"]["right"])

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
            if self.joystick.getRawButton(9):
                self.lift.setSpeed(0.1)
            if self.joystick.getRawButton(11):
                self.lift.setSpeed(-0.1)
            if self.joystick.getRawButton(12):
                self.lift.setSpeed(0)
        except:
            self.onException()

if __name__ == '__main__':
    wpilib.run(Robot)