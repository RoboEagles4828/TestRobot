from enum import Enum
from rev.color import ColorSensorV3


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
        if self.color.red > 0.6:
            return self.Color.RED
        if self.color.green > 0.55:
            return self.Color.GREEN
        if self.color.red < 0.2:
            return self.Color.CYAN
        if self.color.blue < 0.2:
            return self.Color.YELLOW
        return self.Color.NONE

    def execute(self):
        self.color = self.color_sensor.getColor()
