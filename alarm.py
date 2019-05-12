import time
import os
import threading
from traffic_light import TrafficLight, RED, YELLOW, GREEN

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.tl = TrafficLight()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    self.tl.flash_random(10, 0.1)
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False
