from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()
try:

    #tl.kill((RED, YELLOW, GREEN))
    tl.flash_random(5, 0.1)
    tl.kill_all()
    time.sleep(1)

    tl.cycle_down(5, 0.1)
    tl.kill_all()
    time.sleep(1)

    tl.cycle_up(5, 0.1)
    tl.kill_all()
    time.sleep(1)

    tl.build_up(5, 0.1)
    tl.kill_all()
    time.sleep(1)

    tl.build_down(5, 0.1)
    tl.kill_all()
    time.sleep(1)

    tl.slide_up(5, 0.1)
    tl.kill_all()
    time.sleep(1)

except Exception as e:
    tl.end()
    raise e
    time.sleep(5)
time.sleep(2)
print ("before end")
tl.end()


