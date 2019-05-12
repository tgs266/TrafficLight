import time
import os
import threading
from traffic_light import TrafficLight, RED, YELLOW, GREEN

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        print (hours, minutes)
        self.tl = TrafficLight()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):

        while self.keep_running:
            now = time.strftime("%H:%M")
            print (now)
            now = now.split(":")
            h = int(now[0])
            m = int(now[1])
            
            if (h == self.hours and m == self.minutes):
                print("ALARM NOW!")
                self.tl.flash_random(10, 0.1)
                return
        time.sleep(1)
        self.tl.flash(RED, 1)

    def just_die(self):
        self.keep_running = False
