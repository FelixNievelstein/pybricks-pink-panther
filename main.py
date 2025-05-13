from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

hub = PrimeHub()

# Motoren
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

greif_motor = Motor(Port.A)
abstandssensor = UltrasonicSensor(Port.D)
lightOn = True

drive_base = DriveBase(left_motor, right_motor, 56, 114)

# Farbsensor
sensor = ColorSensor(Port.E)
shouldRun = True 

def grab():
    reset_motor()
    move_down()
    run_task(drive_forward())
    move_up()

def drop():
    move_down()
    wait(1000)
    run_task(drive_backward())
    reset_motor()

def reset_motor():
    print("Reset")
    greif_motor.run_target(100, 0)
    wait(1000)

def move_up():
    print("Up")
    greif_motor.run_target(1000, 20, then=Stop.HOLD)

def move_down():
    print("Down")
    greif_motor.run_target(100, -50, then=Stop.HOLD)

async def drive_forward():
    await drive_base.straight(50)
    wait(1000)

async def drive_backward():
    await drive_base.straight(-50)
    wait(1000)

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
                self.angle = self.DEFAULT_ANGLE
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
            drop()
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
                self.angle = self.angle + (self.DEFAULT_ANGLE / 2)
                self.whiteCount = self.angle * -1
                
            else:
                self.left_motor.run(self.base_speed * self.direction)
                self.right_motor.run(self.base_speed * self.direction)
            
            self.whiteCount += 1
            wait(100)
        else:
            grab()
            self.left_motor.run(self.base_speed * 20)
            self.right_motor.run(-self.base_speed * 20)
            self.direction = self.direction * -1
            wait(100)


driver = Driver(left_motor, right_motor, shouldRun, hub)


while shouldRun:
        sensor.detectable_colors([Color.BLACK, Color.WHITE, Color.MAGENTA, Color.VIOLET, Color.YELLOW, Color.BLUE])
        color = sensor.color()
        driver.calcMoving(color)
        abstandssensor.lights.on()
        # Drehgeschwindigkeit setzen (in Grad/Sek)