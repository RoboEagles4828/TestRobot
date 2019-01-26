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
        with open("ports.json") as f:
            self.ports = json.load(f)
        #Lift---------------------------------------------
        self.speed = 0
        self.liftLeft = wpilib.Victor(8)
        self.liftRight = wpilib.Victor(9)
        #DriveTrain---------------------------------------
        self.frontLeft = wpilib.Victor(self.ports["drivetrain"]["frontLeft"])
        self.frontRight = wpilib.Victor(7)
        self.backLeft = wpilib.Victor(0) #Change this back to 8 later
        self.backRight = wpilib.Victor(0) #change this back to 9 later

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
                lift.set(0.1)
            if joystick.getRawButton(11):
                lift.set(-0.1)
            if joystick.getRawButton(12):
                lift.set(0)
        except:
            self.onException()

if __name__ == '__main__':
    wpilib.run(Robot)