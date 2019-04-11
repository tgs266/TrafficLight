import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)

class TrafficLight():

    def __init__(self):
        pass

    def kill(self):
        GPIO.cleanup()

    def start_green(self):
        GPIO.setup(21, GPIO.OUT)

    def kill_green(self):
        GPIO.setup(21, GPIO.IN)

    def flash_green(self, interval):
        self.start_green()
        time.sleep(interval)
        self.kill_green()