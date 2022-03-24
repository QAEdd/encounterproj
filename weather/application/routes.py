from application import app
from flask import jsonify
from random import choice

weather = ['Rain', 'sunshine', 'Storm', 'Windy', 'cloudy']

@app.route('/get-weather', methods=['GET'])
def get_weather():
    weat = choice(weather)
    return jsonify(weat=weat)