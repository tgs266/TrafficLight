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



    def start_yellow(self):
        GPIO.setup(20, GPIO.OUT)

    def kill_yellow(self):
        GPIO.setup(20, GPIO.IN)

    def flash_yellow(self, interval):
        self.start_yellow()
        time.sleep(interval)
        self.kill_yellow()


    
    def start_red(self):
        GPIO.setup(26, GPIO.OUT)

    def kill_red(self):
        GPIO.setup(26, GPIO.IN)

    def flash_red(self, interval):
        self.start_red()
        time.sleep(interval)
        self.kill_red()