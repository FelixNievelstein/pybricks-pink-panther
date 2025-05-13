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
reflectionList = []

while True:
    reflection = sensor.reflection()
    error = reflection - THRESHOLD
    turn = Kp * error
    print(reflection)
    # Drehgeschwindigkeit setzen (in Grad/Sek)
    reflectionList.append(reflection)
    if reflection < BLACK: 
        direction = 1
        left_motor.run(-base_speed)
        right_motor.run(base_speed)    
    elif reflection >= WHITE:
        if whiteCount == 5:
            direction = -1            
            print("change direction")

        left_motor.run((base_speed - turn) * direction)
        right_motor.run((base_speed + turn) * direction)
        whiteCount += 1
    

    wait(10)
