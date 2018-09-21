from flask import Flask, flash, redirect, render_template, request, session, abort
from modifyflows import StaticFlowPusher
import json

pusher = StaticFlowPusher('127.0.0.1')

app = Flask(__name__)


@app.route("/index/")
def index():
    return "Index !"

@app.route("/setRule/")
def my_form():
    return render_template('my-form.html')

@app.route("/setRule/", methods=['POST'])
def my_form_post():
    ip = request.form['ip']
    dpid = request.form['dpid']
    _name = request.form['rule']
    pusher.set({'switch':dpid,"name":_name,"eth_type":"0x0800","ipv4_src":ip,"active":"true"})
    return "*** Rule set ***"


@app.route("/removeRule/")
def my_form2():
    return render_template('my-form.html')

@app.route("/removeRule/", methods=['POST'])
def my_form_post2():
    ip = request.form['ip']
    dpid = request.form['dpid']
    _name = request.form['rule']
    pusher.remove(json, {'switch':dpid,"name":_name,"eth_type":"0x0800","ipv4_src":ip,"active":"true"})
    return "*** Rule Removed ***"

@app.route("/")
def hello():
    return render_template('test.html', name="WELCOME TO FLOODLIGHT APPLICATION")


if __name__== "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
