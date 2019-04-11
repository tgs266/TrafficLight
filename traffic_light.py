import RPi.GPIO as GPIO 
import time 
import random
import threading

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

    def flash_random(self, length, interval):
        for i in [RED, YELLOW, GREEN]:
            t = threading.Thread(target=self.flash_random_thread, args=(length, interval, i))
            t.start()

    def flash_random_thread(self, length, interval, color):
        t = time.time()
        while time.time() - t < length:
            x = random.choice([0, 1])
            if x == 1:
                self.flash(color, interval)
            else:
                time.sleep(interval)

    def cycle_down(self, cycles, interval):
        for i in range(cycles):
            self.flash(RED, interval)
            self.flash(YELLOW, interval)
            self.flash(GREEN, interval)


