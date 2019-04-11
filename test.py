from traffic_light import TrafficLight, RED, YELLOW, GREEN


tl = TrafficLight()

#tl.flash_random(15, 0.1)

tl.start(RED)
time.sleep(1)
tl.flash((RED, YELLOW), 1)


tl.end()