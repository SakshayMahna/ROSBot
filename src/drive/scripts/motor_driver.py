import RPi.GPIO as gpio 
from time import sleep

class MotorDriver:
    def __init__(self, pinA1, pinA2, pinB1, pinB2):
        gpio.setmode(gpio.BCM)
        self.A1 = pinA1
        self.A2 = pinA1
        self.B1 = pinA1
        self.B2 = pinA1
        gpio.setup(self.A1, gpio.OUT)
        gpio.setup(self.A2, gpio.OUT)
        gpio.setup(self.B1, gpio.OUT)
        gpio.setup(self.B2, gpio.OUT)

    def forward(self, sec):
        gpio.output(self.A1, True)
        gpio.output(self.A2, False)
        gpio.output(self.B1, True)
        gpio.output(self.B2, False)
        sleep(sec)
    
    def backward(self, sec):
        gpio.output(self.A1, False)
        gpio.output(self.A2, True)
        gpio.output(self.B1, False)
        gpio.output(self.B2, True)
        sleep(sec)

    def left(self, sec):
        gpio.output(self.A1, False)
        gpio.output(self.A2, True)
        gpio.output(self.B1, True)
        gpio.output(self.B2, False)
        sleep(sec)

    def right(self, sec):
        gpio.output(self.A1, True)
        gpio.output(self.A2, False)
        gpio.output(self.B1, False)
        gpio.output(self.B2, True)
        sleep(sec)

    def __del__(self):
        gpio.cleanup()
