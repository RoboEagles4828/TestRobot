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

    def get_raw_color(self):
        return self.color_sensor.getColor()

    def get_color(self):
        raw_color = self.color_sensor.getColor()
        if raw_color.red > 0.6:
            return self.Color.RED
        if raw_color.green > 0.55:
            return self.Color.GREEN
        if raw_color.red < 0.2:
            return self.Color.CYAN
        if raw_color.blue < 0.2:
            return self.Color.YELLOW
        return self.Color.NONE
