from traffic_light import TrafficLight, RED, YELLOW, GREEN


tl = TrafficLight()

#tl.flash_random(15, 0.1)

tl.start(RED)
tl.flash((RED, YELLOW))


tl.end()