from flask import Flask, render_template, request
from traffic_light import TrafficLight, RED, YELLOW, GREEN

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
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090)