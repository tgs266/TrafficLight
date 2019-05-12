from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time
tl = TrafficLight()

def show_1(length, interval):
    tl.flash_random(length, interval)

def show_2():
    tl.cycle_down(5, 0.5)
