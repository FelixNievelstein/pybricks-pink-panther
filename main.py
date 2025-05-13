from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from .greifen import oeffnen

hub = PrimeHub()

# Motoren
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Farbsensor
sensor = ColorSensor(Port.E)
shouldRun = True 

class Driver:

    DEFAULT_ANGLE = 20 
    base_speed = 250
    whiteCount = 0
    blackCount = 301
    direction = 1
    angle = DEFAULT_ANGLE


    def __init__(self, left_motor, right_motor, run, hub):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.hub = hub
        self.run = run


    def calcMoving(self, color):
        print(color)
        if color == Color.BLACK: 
            # Gerade aus
            if self.blackCount >= 300:
                self.base_speed = 150
                self.angle = DEFAULT_ANGLE
                self.whiteCount = 0
                self.direction = 1
                self.left_motor.run(-self.base_speed)
                self.right_motor.run(self.base_speed)
            else:
                self.base_speed = 20
                self.left_motor.run(self.base_speed * self.direction)
                self.right_motor.run(self.base_speed * self.direction)
            
            self.blackCount += 1
                
        elif color == Color.YELLOW:
            print("Stop Gelb")     
            self.hub.display.text("Juhu")
            self.run = False       
        elif color == Color.WHITE:
            # Kurve
            self.base_speed = 10
            self.blackCount = 0
            print(self.angle)
            print(self.whiteCount)
            if self.whiteCount == self.angle:
                print("change direction")
                self.direction = self.direction * -1
                self.angle = self.angle + (DEFAULT_ANGLE / 2)
                self.whiteCount = self.angle * -1
                
            else:
                self.left_motor.run(self.base_speed * self.direction)
                self.right_motor.run(self.base_speed * self.direction)
            
            self.whiteCount += 1
            wait(100)
        else:
            self.left_motor.run(self.base_speed * 20)
            self.right_motor.run(-self.base_speed * 20)
            self.direction = self.direction * -1
            wait(100)


driver = Driver(left_motor, right_motor, shouldRun, hub)


while shouldRun:
        sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.VIOLET, Color.YELLOW, Color.BLUE])
        color = sensor.color()
        driver.calcMoving(color)
        # Drehgeschwindigkeit setzen (in Grad/Sek)