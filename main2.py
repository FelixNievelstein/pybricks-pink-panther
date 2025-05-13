from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


hub = PrimeHub()

# Farbsensor
sensor = ColorSensor(Port.E)
#my_lila = Color()


while True:     
    sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.VIOLET, Color.YELLOW, Color.BLUE])
    print(sensor.color())
