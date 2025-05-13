from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.tools import run_task


greif_motor = Motor(Port.A)
abstandssensor = UltrasonicSensor(Port.D)

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)

drive_base = DriveBase(left_motor, right_motor, 56, 114)

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

grab()
drop()