from flask import Flask, render_template, request
from traffic_light import TrafficLight, RED, YELLOW, GREEN
import time 

app = Flask(__name__)

tl = TrafficLight()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test1", methods=['GET', 'POST'])
def test1():
    print(request.method)
    if request.method == 'POST':
        if request.form.get("red") == "Red":
            if tl.live[RED] == 1:
                tl.kill(RED)
            else:
                tl.start(RED)
        elif request.form.get("yellow") == "Yellow":
            if tl.live[YELLOW] == 1:
                tl.kill(YELLOW)
            else:
                tl.start(YELLOW)
        elif request.form.get("green") == "Green":
            if tl.live[GREEN] == 1:
                tl.kill(GREEN)
            else:
                tl.start(GREEN)
    return render_template("test1.html")

rec_data = []
time_start = 0
recent = 0
done = True

@app.route("/record", methods=['GET', 'POST'])
def record():
    print(request.method)
    if request.method == 'POST':
        global rec_data, time_start, recent, done
        if request.form.get("record") == "Start" and time_start == 0 and done == False:

                time_start = time.time()
                recent = time_start
        elif request.form.get("red") == "Red" and done == False:
            rec_data.append([RED, time.time() - recent])
            recent = time.time()

        elif request.form.get("yellow") == "Yellow" and done == False:
            rec_data.append([YELLOW, time.time() - recent])
            recent = time.time()
        elif request.form.get("green") == "Green" and done == False:
            rec_data.append([GREEN, time.time() - recent])
            recent = time.time()
        
        if time.time() - time_start > 30:
            time_start = 0
            recent = 0
            done = True 

        if request.form.get("record") == "Stop":
            time_start = 0
            recent = 0
            done = True 
        
        if request.form.get("play") == "Play":
            for i in rec_data:
                tl.start(i[0])
                time.sleep(i[1])
            done = False 

        print(rec_data)
    return render_template("record.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)