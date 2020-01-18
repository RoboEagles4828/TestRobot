"""Main robot module"""
import logging
import sys
import json
import wpilib
#import ctre
from rev.color import ColorSensorV3

#from components.low.drivetrain import Drivetrain
from components.low.color_sensor import ColorSensor


class Robot(wpilib.TimedRobot):
    """Main robot class"""
    def robotInit(self):
        """Robot initialization"""
        self.logger = logging.getLogger("Robot")
        # Load ports and buttons
        with open(sys.path[0] + "/ports.json") as file:
            self.ports = json.load(file)
        with open(sys.path[0] + "/buttons.json") as file:
            self.buttons = json.load(file)
        # Create timer
        self.timer = wpilib.Timer()
        # Create joystick
        self.joystick = wpilib.Joystick(0)
        # Create shuffleboard tab
        #self.test_tab = wpilib.shuffleboard.Shuffleboard.getTab("Test")
        # Launch camera server
        #wpilib.CameraServer.launch()
        # Create drivetrain
        #self.front_left = ctre.TalonSRX(self.ports["drive"]["front_left"])
        #self.front_right = ctre.TalonSRX(self.ports["drive"]["front_right"])
        #self.back_left = ctre.TalonSRX(self.ports["drive"]["back_left"])
        #self.back_right = ctre.TalonSRX(self.ports["drive"]["back_right"])
        #self.drivetrain = Drivetrain(self.front_left, self.front_right,
        #self.back_left, self.back_right)
        # Create color sensor
        self.color_sensor = ColorSensor(ColorSensorV3(
            wpilib.I2C.Port.kOnboard))

    def autonomousInit(self):
        """Autonomous mode initialization"""

    def autonomousPeriodic(self):
        """Autonomous mode periodic (20ms)"""

    def teleopInit(self):
        """Teleoperated mode initialization"""
        self.timer.reset()
        self.timer.start()

    def teleopPeriodic(self):
        """Teleoperated mode periodic (20ms)"""
        # Drive
        #try:
        #    self.drive.setSpeedsFromJoystick(self.joystick.getX(),
        #                                     self.joystick.getY(),
        #                                     self.joystick.getTwist())
        #except:
        #    self.onException()
        if self.timer.hasPeriodPassed(0.5):
            color = self.color_sensor.get_raw_color()
            print("%s: %f:%f:%f" % (self.color_sensor.get_color().name,
                                    color.red, color.green, color.blue))

    def disabledInit(self):
        """Disabled mode initialization"""

    def disabledPeriodic(self):
        """Disabled mode periodic (20ms)"""


logging.basicConfig(level=logging.DEBUG)
if __name__ == "__main__":
    wpilib.run(Robot)
