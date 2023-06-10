from Lights import Light
from Displays import *
from Button import *
import time
from myclasses import *
from SevenSegSingle import *

print("Hello, Pi Pico!")

button1 = Button(0, "Left Side Button", buttonhandler=None)
button2 = Button(13, "Right Side Button", buttonhandler=None)
pir = MotionSensor(28)
red1light = Light(4, "Car1 Red Light")
yellow1light = Light(5, "Car1 Yellow Light")
green1light = Light(6, "Car1 Green Light")
green2light = Light(11, "pedestrian1 Green Light")
red2light = Light(19, "Car2 Red Light")
yellow2light = Light(20, "Car2 Yellow Light")
green3light = Light(21, "Car Green Light")
green4light = Light(27, "pedestrian2 Green Light")

green1light.on()
green3light.on()


class MyModel:
    def __init__(self):
        self._button1 = Button(0, "Left Side Button", buttonhandler=self.button1_press)
        self._button2 = Button(13, "Right Side Button", buttonhandler=self.button2_press)
        self._red1light = Light(4, "Car Red Light")
        self._green2light = Light(11, "pedestrian Green Light")

        self._model = Model(2, self, debug=True)

        self._model.addButton(self._button1)
        self._model.addButton(self._button2)

        self._model.addTransition(0, BTN1_PRESS, 1)
        self._model.addTransition(0, BTN2_PRESS, 1)

    def run(self):
        self._model.run()

    def stateDo(self, state):
        if state == 0:
            if self._pir.motionDetected():
                self._model.gotoState(1)

    def stateEntered(self, state):
        if state == 0:
            print('State 0 entered')
            self._red1light.on()
            self._green2light.off()
        elif state == 1:
            print('State 1 entered')
            self._roomlight.on()
            self._green2light.on()

    def button1_press(self):
        print("Button 1 pressed")

    def button2_press(self):
        print("Button 2 pressed")




while True:


    time.sleep(3)
    green1light.on()
    green3light.on()
    def button1_press():
        if green1light.is_active:
           yellow1light.on()
           time.sleep(2)
           red1light.on()
           red2light.on()
           green2light.on()
           green4light.on()
           time.sleep(2)

    button1.when_pressed = button1_press
    
    green1light.off()
    green3light.off()
    time.sleep(1)

    yellow1light.on()
    yellow2light.on()
    time.sleep(2)
    yellow1light.off()
    yellow2light.off()
    time.sleep(1)

    red1light.on()
    red2light.on()
    green2light.on()
    green4light.on()
    time.sleep(2)

    countDown = SevenSegSingle(dataPin=16, clockPin=18, latchPin=17, commonCathode=False)
    for i in range(5, -1, -1):
        countDown.show(i)
        time.sleep(1)

    time.sleep(2)
    red1light.off()
    red2light.off()
    green2light.off()
    green4light.off()
    time.sleep(1)
