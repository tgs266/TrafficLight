from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()
try:

    tl.kill((RED, YELLOW, GREEN))
    tl.flash_random(5, 0.1)
    # tl.kill(RED)
    # tl.kill(YELLOW)
    # tl.kill(GREEN)
    tl.kill((RED, YELLOW, GREEN))
    # time.sleep(1)
    # tl.cycle_down(5, 0.5)
    # tl.kill((RED, YELLOW, GREEN))
    # time.sleep(1)
    # tl.cycle_up(5, 0.5)
    # tl.kill((RED, YELLOW, GREEN))
    # time.sleep(1)
    # tl.build_up(5, 0.25)
    # tl.kill((RED, YELLOW, GREEN))
    # time.sleep(1)
    # tl.build_down(5, 0.25)
    # tl.kill((RED, YELLOW, GREEN))
    # time.sleep(1)
    # tl.slide_up(5, 0.25)
    # tl.kill((RED, YELLOW, GREEN))
except:
    tl.end()
tl.end()


