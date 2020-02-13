from enum import Enum
from rev.color import ColorSensorV3

import config


class ColorSensor:
    class Color(Enum):
        NONE = 0
        RED = 1
        GREEN = 2
        CYAN = 3
        YELLOW = 4

    def __init__(self, color_sensor: ColorSensorV3, wheel: bool):
        self.color_sensor = color_sensor
        self.wheel = wheel
        self.raw_color = None
        self.color = self.Color.NONE
        self.data = list()
        self.status = False
        self.target = None

    def get_raw_color(self):
        return self.raw_color

    def get_color(self):
        return self.color

    def to_color(self, color: Color):
        self.status = True
        self.target = color

    def cycle_color(self):
        self.to_color(self.get_color())

    def execute(self):
        # Get raw color
        color = self.color_sensor.getColor()
        if color.green > config.ColorSensor.CYAN_GREEN_MIN and color.blue > config.ColorSensor.CYAN_BLUE_MIN:
            self.raw_color = self.Color.CYAN
        elif color.red > config.ColorSensor.YELLOW_RED_MIN and color.green > config.ColorSensor.YELLOW_GREEN_MIN:
            self.raw_color = self.Color.YELLOW
        elif color.red > config.ColorSensor.RED_MIN:
            self.raw_color = self.Color.RED
        elif color.green > config.ColorSensor.GREEN_MIN:
            self.raw_color = self.Color.GREEN
        else:
            self.raw_color = self.Color.NONE
        # Add data
        self.data.append(self.get_raw_color())
        # Drop old data
        if len(self.data) > config.ColorSensor.FILTER_PERIOD + 1:
            self.data.pop(0)
        # Set filtered color
        if len(set(self.data)) == 1:
            self.color = self.data[0]
        # Check wheel status
        if self.status:
            self.wheel = True
            if self.get_color() == self.target:
                self.wheel = False
