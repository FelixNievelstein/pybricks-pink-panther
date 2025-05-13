from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


hub = PrimeHub()

# Farbsensor
sensor = ColorSensor(Port.E)
#my_lila = Color()

OUR_BLUE = (46, Color.BLUE)
OUR_LILA = (26, Color.BLUE)
OUR_BLACK = ()


while True:     
    #sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.YELLOW, Color.BLUE])
    ref = sensor.reflection()
    color = sensor.color()
    print(ref, color)