from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()
try:

    i = 0.2

    tl.flash_random(5, i)
    tl.kill_all()
    time.sleep(1)

    tl.cycle_down(5, i)
    tl.kill_all()
    time.sleep(1)

    tl.cycle_up(5, i)
    tl.kill_all()
    time.sleep(1)

    tl.build_up(5, i)
    tl.kill_all()
    time.sleep(1)

    tl.build_down(5, i)
    tl.kill_all()
    time.sleep(1)


except Exception as e:
    tl.end()
    raise e
    time.sleep(5)
time.sleep(2)
print ("before end")
tl.end()


