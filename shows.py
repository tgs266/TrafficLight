from traffic_light import TrafficLight, RED, YELLOW, GREEN
tl = TrafficLight()

tl.flash_random(10, 0.1)
tl.cycle_down(5, 0.5)
tl.cycle_up(5, 0.5)
tl.build_up(5, 0.25)
tl.build_down(5, 0.25)