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

class Driver:

    base_speed = 250
    whiteCount = 0
    direction = 1

    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor


    def calcMoving(self, color):
        print(color)
        if color == Color.BLACK: 
            self.base_speed = 250
            direction = 1
            self.left_motor.run(-self.base_speed)
            self.right_motor.run(self.base_speed)
        elif color == Color.YELLOW:
            print("Stop Gelb")
        elif color == Color.WHITE:
            self.base_speed = 5
            if self.whiteCount == 50:
                self.direction = self.direction * -1
                print("change direction")
                self.whiteCount = 0

            self.left_motor.run(self.base_speed * self.direction)
            self.right_motor.run(self.base_speed * self.direction)
            self.whiteCount += 1
            wait(100)

driver = Driver(left_motor, right_motor)


while True:
        sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.VIOLET, Color.YELLOW, Color.BLUE])
        color = sensor.color()
        driver.calcMoving(color)
        # Drehgeschwindigkeit setzen (in Grad/Sek)