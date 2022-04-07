from application import app
from flask import jsonify
from random import choice

weather = ['Rain', 'Sunshine', 'Storm', 'Windy', 'Cloudy']

@app.route('/get-weather', methods=['GET'])
def get_weather():
    weat = choice(weather)
    return jsonify(weat=weat)