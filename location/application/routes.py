from application import app
import requests
from flask import jsonify
from random import choice

locations = ["Forest","On the road","Fields","Volcano","Tavern","Cemetery","The void","just over there"]

@app.route('/get-location', methods=['GET'])
def get_location():
    location = choice(locations)
    return jsonify(location=location)