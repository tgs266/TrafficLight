from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time
tl = TrafficLight()

def show_1(length, interval):
    tl.flash_random(length, interval)

def show_2():
    tl.flash(RED, 1)
    tl.start(RED)
    time.sleep(.5)
    tl.flash(YELLOW, 1)
    tl.kill(RED)
