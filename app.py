from flask import Flask
from flask import request
from listener import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Waiting for requests...'

@app.route('/aqi25', methods=['GET'])
def aqi25():
    error = None
    if request.method == 'GET':
        return listener25()
    
@app.route('/aqi10', methods=['GET'])
def aqi10():
    error = None
    if request.method == 'GET':
        return listener10()
    
@app.route('/aqi100', methods=['GET'])
def aqi100():
    error = None
    if request.method == 'GET':
        return listener100()