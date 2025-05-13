from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

# Motoren
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Farbsensor
sensor = ColorSensor(Port.E)

# Reflektionswerte
BLACK = 10
WHITE = 98
LILA = 30
YELLOW = 89
BLUE = 57
THRESHOLD = (BLACK + WHITE) / 2

Kp = 1.0
base_speed = 200

while True:
    reflection = sensor.reflection()
    print(reflection)
    error = reflection - THRESHOLD
    turn = Kp * error

    # Drehgeschwindigkeit setzen (in Grad/Sek)
    # left_motor.run(base_speed - turn)
    # right_motor.run(base_speed + turn)

    wait(10)
