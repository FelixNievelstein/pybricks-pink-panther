from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait


hub = PrimeHub()

# Motoren
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Farbsensor
sensor = ColorSensor(Port.E)
sensor.lights.off()

# Reflektionswerte
BLACK = 15
WHITE = 98
LILA = 30
YELLOW = 89
BLUE = 57
THRESHOLD = (BLACK + WHITE) / 2

Kp = 1.0
base_speed = 50
whiteCount = 0
direction = 1
reflection1 = 0
reflection2 = 0
reflection3 = 0
reflection4 = 0
reflection5 = 0

def calcMoving(color):
    print(color)
    if color == Color.BLACK: 
        direction = 1
        left_motor.run(-base_speed)
        right_motor.run(base_speed)
    elif color == Color.YELLOW:
        print("Stop Gelb")   
    elif color == Color.WHITE:
        if whiteCount == 5:
            direction = -1            
            print("change direction")

        left_motor.run(base_speed - direction)
        right_motor.run(base_speed + direction)
        whiteCount += 1

while True:
    sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.VIOLET, Color.YELLOW, Color.BLUE])
    color = sensor.color()
    # Drehgeschwindigkeit setzen (in Grad/Sek)

    wait(10)