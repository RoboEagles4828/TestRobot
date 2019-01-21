import magicbot 
import wpilib

from components.low.drivetrain import DriveTrain

class Robot(magicbot.MagicRobot):
    drive: DriveTrain
    joystick: wpilib.Joystick

    def createObjects(self):
        self.frontLeft = wpilib.VictorSP(6)
        self.frontRight = wpilib.VictorSP(7)
        self.backLeft = wpilib.VictorSP(8)
        self.backRight = wpilib.VictorSP(9)
    
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        with self.consumeExceptions():
            self.drive.set(self.joystick.getX, self.joystick.getY, self.joystick.getY, self.joystick.getTwist)

if __name__ == '__main__':
    wpilib.run(Robot)