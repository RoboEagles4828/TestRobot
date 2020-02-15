"""Main robot module"""
import logging
import wpilib
import ctre
import rev
import navx

import config
from components.low.analog_input import AnalogInput
from components.low.digital_input import DigitalInput
from components.low.drivetrain import Drivetrain
from components.low.color_sensor import ColorSensor


class Robot(wpilib.TimedRobot):
    """Main robot class"""
    def robotInit(self):
        """Robot initialization"""
        # Create logger
        self.logger = logging.getLogger("Robot")
        # Create timer
        self.timer = wpilib.Timer()
        # Create navx
        self.navx = navx.AHRS.create_spi()
        # Create camera server
        wpilib.CameraServer.launch()
        # Create components list
        self.components = list()
        # Create joystick
        self.joystick = wpilib.Joystick(0)
        self.joystick_x = AnalogInput(
            self.joystick.getX,
            deadzone=config.Robot.JOYSTICK_DEADZONE,
            average_period=config.Robot.JOYSTICK_AVERAGE_PERIOD)
        self.components.append(self.joystick_x)
        self.joystick_y = AnalogInput(
            self.joystick.getY,
            map_a=-1,
            deadzone=config.Robot.JOYSTICK_DEADZONE,
            average_period=config.Robot.JOYSTICK_AVERAGE_PERIOD)
        self.components.append(self.joystick_y)
        self.joystick_twist = AnalogInput(
            self.joystick.getTwist,
            deadzone=config.Robot.JOYSTICK_DEADZONE,
            average_period=config.Robot.JOYSTICK_AVERAGE_PERIOD)
        self.components.append(self.joystick_twist)
        # Create drivetrain
        left_0 = ctre.WPI_TalonSRX(config.Ports.Drivetrain.LEFT_0)
        left_1 = ctre.WPI_TalonSRX(config.Ports.Drivetrain.LEFT_1)
        right_0 = ctre.WPI_TalonSRX(config.Ports.Drivetrain.RIGHT_0)
        right_1 = ctre.WPI_TalonSRX(config.Ports.Drivetrain.RIGHT_1)
        self.drivetrain = Drivetrain(left_0, left_1, right_0, right_1)
        self.components.append(self.drivetrain)
        # Create color sensor
        self.color_sensor = ColorSensor(
            rev.color.ColorSensorV3(wpilib.I2C.Port.kOnboard))
        self.components.append(self.color_sensor)
        self.navx.resetDisplacement()

    def autonomousInit(self):
        """Autonomous mode initialization"""
        self.pos1 = False
        self.pos2 = False
        self.navx.reset()
        self.navx.resetDisplacement()

    def autonomousPeriodic(self):
        """Autonomous mode periodic (20ms)"""
        # Run each component's execute function
        for component in self.components:
            try:
                component.execute()
            except Exception as exception:
                self.logger.exception(exception)
        # Auton mode 1
        try:
            if self.navx.getDisplacementY() <= .01 and not self.pos1:
                self.drivetrain.set_speeds(0.2, 0.2)
            elif self.navx.getAngle() % 360 <= 90:
                self.pos1 = True
                self.navx.resetDisplacement()
                self.drivetrain.set_speeds(-0.2, 0.2)
            elif self.navx.getDisplacementY() <= .017 and not self.pos2:
                self.drivetrain.set_speeds(0.2, 0.2)
            elif self.navx.getAngle() % 360 >= 0:
                self.pos2 = True
                self.navx.resetDisplacement()
                self.drivetrain.set_speeds(0.2, -0.2)
            elif self.navx.getDisplacementY() <= 0.005:
                self.drivetrain.set_speeds(0.2, 0.2)
            else:
                self.drivetrain.set_speeds(0, 0)
            self.logger.info("%f", self.navx.getDisplacementY())
        except Exception as exception:
            self.logger.exception(exception)

    def teleopInit(self):
        """Teleoperated mode initialization"""
        self.timer.reset()
        self.timer.start()

    def teleopPeriodic(self):
        """Teleoperated mode periodic (20ms)"""
        # Run each component's execute function
        for component in self.components:
            try:
                component.execute()
            except Exception as exception:
                self.logger.exception(exception)
        # Drivetrain
        try:
            self.drivetrain.set_speeds_joystick(self.joystick_x.get(),
                                                self.joystick_y.get(),
                                                self.joystick_twist.get())
            self.logger.info("%s %s %s", self.joystick_x.get(),
                             self.joystick_y.get(), self.joystick_twist.get())
        except Exception as exception:
            self.logger.exception(exception)
        # Color sensor
        try:
            color = self.color_sensor.get_raw_color()
            self.logger.info("%s: %f %f %f",
                             self.color_sensor.get_color().name, color.red,
                             color.green, color.blue)
        except Exception as exception:
            self.logger.exception(exception)

    def disabledInit(self):
        """Disabled mode initialization"""

    def disabledPeriodic(self):
        """Disabled mode periodic (20ms)"""


logging.basicConfig(level=logging.DEBUG)
if __name__ == "__main__":
    wpilib.run(Robot)
