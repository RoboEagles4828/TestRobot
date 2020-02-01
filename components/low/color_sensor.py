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

    def __init__(self, color_sensor: ColorSensorV3):
        self.color_sensor = color_sensor
        self.color = None

    def get_raw_color(self):
        return self.color

    def get_color(self):
        if self.color.green > config.ColorSensor.CYAN_GREEN_MIN and self.color.blue > config.ColorSensor.CYAN_BLUE_MIN:
            return self.Color.CYAN
        if self.color.red > config.ColorSensor.YELLOW_RED_MIN and self.color.green > config.ColorSensor.YELLOW_GREEN_MIN:
            return self.Color.YELLOW
        if self.color.red > config.ColorSensor.RED_MIN:
            return self.Color.RED
        if self.color.green > config.ColorSensor.GREEN_MIN:
            return self.Color.GREEN
        return self.Color.NONE

    def execute(self):
        self.color = self.color_sensor.getColor()
