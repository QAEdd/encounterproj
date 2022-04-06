from application import app
import requests
from flask import render_template, url_for

@app.route('/')
def index():
    location_ = requests.get('http://location:5000/get-location')
    weather_ = requests.get('http://weather:5000/get-weather')
    mobs_ = requests.post('http://mobs:5000/get-mobs', json=location_.json())
    results = "you will be fighting " + mobs_.json() + " by a " + location_.json() + "while the weather is " + weather_.json() 
    return render_template('index.html', results = results)