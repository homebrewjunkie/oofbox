from flask import Flask, render_template, request
import socket, os, time

#Load sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rtm = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Create the local flask app to relay w/ PS4
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<path:injection>")
def webkit(injection):
    if injection == "antiban":
        return render_template("antiban.html")
    elif injection == "antilag":
        return "[/] AntiLag AntiRoute Active"
    elif injection == "radarbug":
        return "[/] RadarBug activated [/] local.pss Routed"


#Run the WebApp w/ debug on Localhost:8080
app.run(host="localhost", port=8080, debug=True)
