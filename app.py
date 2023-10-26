from flask import Flask
from flask import request
from flask_cors import CORS
from listener import *

app = Flask(__name__)
CORS(app)

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

@app.route('/it', methods=['GET'])
def it():
    error = None
    if request.method == 'GET':
        return listener_it()

@app.route('/io', methods=['GET'])
def io():
    error = None
    if request.method == 'GET':
        return listener_io()
    
@app.route('/ot', methods=['GET'])
def ot():
    error = None
    if request.method == 'GET':
        return listener_ot()

@app.route('/oh', methods=['GET'])
def oh():
    error = None
    if request.method == 'GET':
        return listener_oh()