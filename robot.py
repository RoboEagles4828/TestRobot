import json
import sys
import logging
import magicbot
import wpilib
from wpilib.shuffleboard import Shuffleboard
import ctre

from components.low.drivetrain import DriveTrain
from components.low.arm import Arm

class Robot(magicbot.MagicRobot):

    drive: DriveTrain
    arm: Arm

    def createObjects(self):
        self.logger = logging.getLogger("Robot")
        # Load ports and buttons
        with open(sys.path[0] + "/ports.json") as f:
            self.ports = json.load(f)
        with open(sys.path[0] + "/buttons.json") as f:
            self.buttons = json.load(f)
        # Drive
        self.front_left = wpilib.Spark(self.ports["drive"]["front_left"])
        self.front_right = wpilib.Spark(self.ports["drive"]["front_right"])
        self.back_left = wpilib.Spark(self.ports["drive"]["back_left"])
        self.back_right = wpilib.Spark(self.ports["drive"]["back_right"])
        # Arm
        self.arm_left = ctre.WPI_TalonSRX(self.ports["arm"]["arm_left"])
        self.arm_right = ctre.WPI_TalonSRX(self.ports["arm"]["arm_right"])
        self.wrist = ctre.WPI_TalonSRX(self.ports["arm"]["wrist"])
        self.intake = ctre.WPI_TalonSRX(self.ports["arm"]["intake"])
        self.hatch = wpilib.DoubleSolenoid(self.ports["arm"]["hatch_in"], self.ports["arm"]["hatch_out"])
        # Joystick
        self.joystick = wpilib.Joystick(0)
        # Timer
        self.printTimer = wpilib.Timer()
        self.printTimer.start()
        # Shuffleboard
        self.test_tab = Shuffleboard.getTab("Test")
        # CameraServer
        wpilib.CameraServer.launch()

    def teleopInit(self):
        print("Starting Teleop")

    def teleopPeriodic(self):
        # Drive
        try:
            self.drive.setSpeedsFromJoystick(self.joystick.getX(), self.joystick.getY(), self.joystick.getTwist())
        except:
            self.onException()
        # Arm
        try:
            if self.joystick.getRawButton(self.buttons["arm"]["arm_up"]):
                self.arm.setSpeed(0.3)
            elif self.joystick.getRawButton(self.buttons["arm"]["arm_down"]):
                self.arm.setSpeed(-0.3)
            else:
                self.arm.setSpeed(0)
        except:
            self.onException()
        # Wrist
        try:
            if self.joystick.getRawButton(self.buttons["arm"]["wrist_up"]):
                self.arm.setWristSpeed(-0.9)
            elif self.joystick.getRawButton(self.buttons["arm"]["wrist_down"]):
                self.arm.setWristSpeed(0.9)
            else:
                self.arm.setWristSpeed(0)
        except:
            self.onException()
        # Intake
        try:
            if self.joystick.getRawButton(self.buttons["arm"]["intake_in"]):
                self.arm.setIntakeSpeed(-1.0)
            elif self.joystick.getRawButton(self.buttons["arm"]["intake_out"]):
                self.arm.setIntakeSpeed(1.0)
            else:
                self.arm.setIntakeSpeed(0)
        except:
            self.onException()
        # Hatch
        try:
            self.arm.setHatch(self.joystick.getRawButton(self.buttons["arm"]["hatch"]))
        except:
            self.onException()
        # Encoders
        try:
            if self.printTimer.hasPeriodPassed(0.5):
                self.logger.info(self.arm.getEnc())
        except:
            self.onException()

    def testInit(self):
        print("Starting Test")
        self.test_speed = (
            self.test_tab
            .add(title="Speed", value=0.1)
            .withWidget("Number Slider")
        )

    def testPeriodic(self):
        pass

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    wpilib.run(Robot)
