import json
import os, sys
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

        #wd = print(os.path.dirname(os.path.realpath(__file__)))
        with open("../ports.json" if os.getcwd()[-5:-1] == "test" else sys.path[0] + "/ports.json") as f:
            self.ports = json.load(f)
        with open("../buttons.json" if os.getcwd()[-5:-1] == "test" else sys.path[0] + "/buttons.json") as f:
            self.buttons = json.load(f)
        # Arm
        arm_ports = self.ports["arm"]
        self.arm_left = ctre.WPI_TalonSRX(arm_ports["arm_left"])
        self.arm_right = ctre.WPI_TalonSRX(arm_ports["arm_right"])
        self.wrist = ctre.WPI_TalonSRX(arm_ports["wrist"])
        self.intake = ctre.WPI_TalonSRX(arm_ports["intake"])
        self.hatch = wpilib.DoubleSolenoid(arm_ports["hatch_in"], arm_ports["hatch_out"])
        # DriveTrain
        drive_ports = self.ports["drive"]
        self.front_left = wpilib.Spark(drive_ports["front_left"])
        self.front_right = wpilib.Spark(drive_ports["front_right"])
        self.back_left = wpilib.Spark(drive_ports["back_left"])
        self.back_right = wpilib.Spark(drive_ports["back_right"])

        self.joystick = wpilib.Joystick(0)

        self.printTimer = wpilib.Timer()
        self.printTimer.start()
        self.test_tab = Shuffleboard.getTab("Test")
        wpilib.CameraServer.launch()

    def teleopInit(self):
        print("Teleop Started!")

    def teleopPeriodic(self):
        try:
            self.drive.set(self.joystick.getX() / 3, self.joystick.getY() / 3, self.joystick.getTwist() / 3)
        except:
            self.onException()
        try:
            # Arm
            arm_buttons = self.buttons["arm"]
            if self.joystick.getRawButton(arm_buttons["arm_up"]):
                self.arm.setSpeed(0.3)
            elif self.joystick.getRawButton(arm_buttons["arm_down"]):
                self.arm.setSpeed(-0.3)
            else:
                self.arm.setSpeed(0)
        except:
            self.onException()
        try:
            # Wrist
            if self.joystick.getRawButton(arm_buttons["wrist_up"]):
                self.arm.setWristSpeed(-.9)
            elif self.joystick.getRawButton(arm_buttons["wrist_down"]):
                self.arm.setWristSpeed(.9)
            else:
                self.arm.setWristSpeed(0)
        except:
            self.onException()
        try:
            # Intake
            if self.joystick.getRawButton(arm_buttons["intake_in"]):
                self.arm.setIntakeSpeed(-1)
            elif self.joystick.getRawButton(arm_buttons["intake_out"]):
                self.arm.setIntakeSpeed(1)
            else:
                self.arm.setIntakeSpeed(0)
        except:
            self.onException()
        try:
            # Hatch
            self.arm.setHatch(self.joystick.getRawButton(arm_buttons["hatch"]))
        except:
            self.onException()

        try:
            # Encoders
            if self.printTimer.hasPeriodPassed(0.5):
                self.logger.info(self.arm.getEncVal())
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
        self.arm_right.set(self.test_speed.getDouble(1.0))
        self.wrist.set(self.test_speed.getDouble(1.0))

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    wpilib.run(Robot)
