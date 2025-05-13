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

def calcMoving(reflection):
    print(reflection)
    if reflection < BLACK: 
        direction = 1
        left_motor.run(-base_speed)
        right_motor.run(base_speed)
    elif reflection == 30:
        print("Stop LILA")   
    elif reflection >= WHITE:
        if whiteCount == 5:
            direction = -1            
            print("change direction")

        left_motor.run((base_speed - turn) * direction)
        right_motor.run((base_speed + turn) * direction)
        whiteCount += 1

def getAverage():
    return (reflection1 + reflection2 + reflection3 + reflection4 + reflection5) / 5

while True:
    reflection = sensor.reflection()
    error = reflection - THRESHOLD
    turn = Kp * error
    # Drehgeschwindigkeit setzen (in Grad/Sek)

    print(sensor.color())

    currentRef = getAverage()
    calcMoving(currentRef)

    wait(10)