import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

RED = 26
YELLOW = 20
GREEN = 21

class TrafficLight():

    def __init__(self):
        pass

    def end(self):
        GPIO.cleanup()

    def start(self, channels):
        GPIO.setup(channels, GPIO.OUT)

    def kill(self, channels):
        GPIO.setup(channels, GPIO.IN)

    def flash(self, channels, interval):
        self.start(channels)
        time.sleep(interval)
        self.kill(channels)

    def cycle_down(self, cycles, interval):
        for i in range(cycles):
            self.flash(RED, interval)
            self.flash(YELLOW, interval)
            self.flash(GREEN, interval)


