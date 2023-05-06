from Lights import Light
from Buzzer import *
from Displays import *
import time

print("Hello, Pi Pico")

led = Light(25, "Onboard LED")

led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)

redled = Light (0,"Red light")

redled.on()
time.sleep(1)
redled.off()
time.sleep(1)

buzz = PassiveBuzzer(13)
buzz.play()
time.sleep(1)
buzz.stop()

display = LCDDisplay(sda = 20, scl = 21, i2cid = 0)
display.showText("Life is good")