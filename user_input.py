from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()

R_active = False
Y_active = False
G_active = False

while True:
    channel = int(input("R (1), Y (2), G (3), EXIT (4): "))
    if channel == 1:
        if R_active:
            tl.kill(RED)
            R_active = False
        else:
            tl.start(RED)
            R_active = True 

    elif channel == 2:
        if Y_active:
            tl.kill(YELLOW)
            Y_active = False
        else:
            tl.start(YELLOW)
            Y_active = True 

    elif channel == 3:
        if G_active:
            tl.kill(GREEN)
            R_active = False
        else:
            tl.start(GREEN)
            G_active = True 

    elif channel == 4:
        tl.end()
        break