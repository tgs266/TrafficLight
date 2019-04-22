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

@app.route("/record", methods=['GET', 'POST'])
def record():
    print(request.method)
    if request.method == 'POST':
        global rec_data, time_start, recent
        if request.form.get("record") == "Start" and time_start == 0:

                time_start = time.time()
                recent = time_start
        elif request.form.get("red") == "Red":
            rec_data.append([RED, time.time() - recent])
            recent = time.time()

        elif request.form.get("yellow") == "Yellow":
            rec_data.append([YELLOW, time.time() - recent])
            recent = time.time()
        elif request.form.get("green") == "Green":
            rec_data.append([GREEN, time.time() - recent])
            recent = time.time())
        print(rec_data)
    return render_template("record.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)