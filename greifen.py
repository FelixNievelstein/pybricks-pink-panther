from pybricks.pupdevices import Motor, DistanceSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

greif_motor = Motor(Port.A)  # z.B. Port A für den Greifarm
abstandssensor = DistanceSensor(Port.D)

def oeffnen():
    print("Oeffnen...")
    greif_motor.run_target(500, -90, then=Stop.HOLD)  # -90° für Schließen (je nach Bauweise anpassen)

def greifen():
    print("Greifen...")
    greif_motor.run_target(500, -90, then=Stop.HOLD)  # -90° für Schließen (je nach Bauweise anpassen)

while True:
    greifen()
    wait(1000)  
    oeffnen()
    wait(1000)    
