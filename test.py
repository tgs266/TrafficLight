from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()

#tl.flash_random(1, 0.1)
tl.cycle_down(2, .5)

tl.end()