from application import app
import requests
from flask import request, jsonify
from random import choice

mobs = ['Dragon','Goblins','Owlbear','Fire Giant']

@app.route('/get-mobs', methods=['POST'])
def get-mob():
    request_ = requests.json()
    if request_ == "Volcano":
        mobs.append('Fire Giant')
        mobs.append('Fire Giant')
    elif request_ == "Forest"
        mobs.append('Owlbear')
        mobs.append('Owlbear')
    elif request_ == "On the road"
        mobs.append('Goblin')
        mobs.append('Goblin')
    elif request_ == 'Tavern'
        mobs.append('Dragon')
        mobs.append('Dragon')
    mob = choice(mobs)
    return json(mob)

 
