import json
import os
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
        with open("../ports.json" if os.getcwd()[-5:-1] == "test" else "ports.json") as f:
            self.ports = json.load(f)
        with open("../buttons.json" if os.getcwd()[-5:-1] == "test" else "buttons.json") as f:
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

        self.print_timer = wpilib.Timer()
        self.print_timer.start()
        self.logger = logging.getLogger("Robot")
        self.test_tab = Shuffleboard.getTab("Test")
        wpilib.CameraServer.launch()

    def teleopInit(self):
        print("Teleop Started!")

    def teleopPeriodic(self):
        try:
            self.drive.set(self.joystick.getX(), self.joystick.getY(), self.joystick.getTwist())
            # Arm
            if self.joystick.getRawButton(buttons["arm_up"]):
                self.arm.setSpeed(0.3)
            elif self.joystick.getRawButton(buttons["arm_down"]):
                self.arm.setSpeed(-0.3)
            else:
                self.arm.setSpeed(0)
            # Wrist
            if self.joystick.getRawButton(buttons["wrist"]):
                self.arm.setWristSpeed(0.3)
            else:
                self.arm.setWristSpeed(0)
            # Intake
            if self.joystick.getRawButton(buttons["intake_in"]):
                self.arm.setIntakeSpeed(-1)
            elif self.joystick.getRawButton(buttons["intake_out"]):
                self.arm.setIntakeSpeed(1)
            else:
                self.arm.setIntakeSpeed(0)
            # Hatch
            self.arm.setHatch(self.joystick.getRawButton(buttons["hatch"]))
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
