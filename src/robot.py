import magicbot 
import wpilib
import json

from components.low.drivetrain import DriveTrain

import logging
logging.basicConfig(level=logging.DEBUG)

class Robot(magicbot.MagicRobot):

    drive: DriveTrain

    def createObjects(self):
        with open("ports.json") as f:
            self.ports = json.load(f)
        
        self.frontLeft = wpilib.Victor(self.ports["drivetrain"]["frontLeft"])
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
        except:
            self.onException()

if __name__ == '__main__':
    wpilib.run(Robot)