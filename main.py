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

def shouldCalcMoving():
    len(reflectionList) > 10

def getAverage():
    return sum(reflectionList) / len(reflectionList)

while True:
    reflection = sensor.reflection()
    error = reflection - THRESHOLD
    turn = Kp * error
    # Drehgeschwindigkeit setzen (in Grad/Sek)
    reflectionList.append(reflection)
    shouldCalc = shouldCalcMoving()
    if shouldCalc:
        currentRef = getAverage()
        reflectionList.clear()
        calcMoving(currentRef)      