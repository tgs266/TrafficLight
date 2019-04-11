from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time

tl = TrafficLight()

R_active = False
Y_active = False
G_active = False

def activate(channel, R_active, Y_active, G_active):
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
            G_active = False
        else:
            tl.start(GREEN)
            G_active = True 

    return R_active, Y_active, G_active
    

while True:
    channel = str(input("R (1), Y (2), G (3), EXIT (4): "))
    if len(channel) == 1:
        channel = int(channel)
        if channel == 4:
            tl.end()
            break 
        else:
            R_active, Y_active, G_active = activate(channel, R_active, Y_active, G_active)
    else:
        channel = channel.split("|")
        print (channel)
        if len(channel) == 1:
            interval = 0.25
        else:
            interval = float(channel[-1])
        channel = channel[0]
        for i in channel:
            i = int(i)
            R_active, Y_active, G_active = activate(i, R_active, Y_active, G_active)
            time.sleep(interval)