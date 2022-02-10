from gamepad import XboxController
from time import sleep


joy = XboxController()
while True:
    print(joy.readMainButtons())
    print(joy.readTriggers())
    print(joy.readAnalogSticks())
    sleep(0.25)
