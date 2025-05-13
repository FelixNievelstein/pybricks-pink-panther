from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

# declare the hardware attached to the robot
hub = PrimeHub()
color = ColorSensor('E')
motors = MotorPair('B', 'C')

# parameters, adjust as necessary
lo_light = 7  # average amount of light next to line
hi_light = 20 # average amount of light on the line
turn_max = 50 # tightness of turning, less values drive straighter

# turn and find the line
while(color.get_reflected_light() < hi_light - 3):
    motors.start_at_power(66, -25)

# stop the motors from the previous operation
motors.stop()

# scales an input to the specified bounds
# essentially an y = mx + b equation
def scale(amt):
    in_min  =  lo_light
    in_max  =  hi_light
    out_min = -turn_max
    out_max =  turn_max
    return (amt - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# main loop, replace True with your condition for stopping
while(True):
    # calculate turn amount based on light value
    color_amt = color.get_reflected_light()
    turn_amt = scale(color_amt)

    # move the motors at 50% power and the specified turning amount
    # drives without a set distance so that it does not jerk while moving
    motors.start_at_power(50, int(turn_amt)) # cast turn_amt to int

    # print values to SPIKE App console for debugging
    print('Color input: {} | Turn amount: {}'.format(color_amt, turn_amt))