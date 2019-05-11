from flask import Flask, render_template, request
from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time 

app = Flask(__name__)

tl = TrafficLight()

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/", methods=['GET', 'POST'])
def home():
    # print(request.method)
    # if request.method == 'POST':
    #     if request.form.get("red") == "Red":
    #         hit(RED)
    #     elif request.form.get("yellow") == "Yellow":
    #         hit(YELLOW)
    #     elif request.form.get("green") == "Green":
    #         hit(GREEN)
    return render_template("home.html")

def hit(channel):
    if tl.live[channel] == 1:
        tl.kill(channel)
    else:
        tl.start(channel)

def random():
    tl.flash_random(10, 0.1)

rec_data = []
time_start = 0
recent = 0
done = False

@app.route("/<cmd>")
def comm(cmd=None):
    print ("test")
    print (cmd)
    if cmd == RED or cmd == "RED":
        hit(RED)
    elif cmd == YELLOW or cmd == "YELLOW":
        hit(YELLOW)
    elif cmd == GREEN or cmd == "GREEN":
        hit(GREEN)
    elif cmd == "RANDOM":
        print ("rand")
        random()
    
    return ('', 204)

@app.route("/record/<cmd>")
def comm_record(cmd=None):
    global rec_data, time_start, recent, done
    print ("test")
    if cmd == RED or cmd == "RED":
        rec_data.append([RED, time.time() - recent])
        recent = time.time()
    elif cmd == YELLOW or cmd == "YELLOW":
        rec_data.append([YELLOW, time.time() - recent])
        recent = time.time()
    elif cmd == GREEN or cmd == "GREEN":
        rec_data.append([GREEN, time.time() - recent])
        recent = time.time()
    elif cmd == "STOP":
        time_start = 0
        recent = 0
        done = True 
    elif cmd == "PLAY":

        for i in rec_data:
            hit(i[0])
            time.sleep(i[1])
        done = False 
        rec_data = []

    elif cmd == "START" and time_start == 0 and done == False:
        time_start = time.time()
        recent = time_start
        
    return ('', 204)
    

@app.route("/record", methods=['GET', 'POST'])
def record():
    print(request.method)
    if request.method == 'POST':
        global rec_data, time_start, recent, done
        
        # elif request.form.get("red") == "Red" and done == False:
        #     rec_data.append([RED, time.time() - recent])
        #     recent = time.time()

        # elif request.form.get("yellow") == "Yellow" and done == False:
        #     rec_data.append([YELLOW, time.time() - recent])
        #     recent = time.time()
        # elif request.form.get("green") == "Green" and done == False:
        #     rec_data.append([GREEN, time.time() - recent])
        #     recent = time.time()
        
        if time.time() - time_start > 30:
            time_start = 0
            recent = 0
            done = True 
            
        
        

        print(rec_data)
    return render_template("record.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)