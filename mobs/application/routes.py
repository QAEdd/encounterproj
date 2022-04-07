from application import app
import requests
from flask import request, jsonify
from random import choice



@app.route('/get-mobs', methods=['POST'])
def get_mob():
    request_json = request.get_json()
    request_ = request_json['location']
    mobs = ['Dragon','Goblin Horde','Owlbear','Fire Giant']
    if request_ == "Volcano":
        mobs.append('Fire Giant')
        mobs.append('Fire Giant')
        mobs.append('Fire Giant')
        mobs.append('Fire Giant')
    elif request_ == "Forest":
        mobs.append('Owlbear')
        mobs.append('Owlbear')
        mobs.append('Owlbear')
        mobs.append('Owlbear')
    elif request_ == "On the road":
        mobs.append('Goblin Horde')
        mobs.append('Goblin Horde')
        mobs.append('Goblin Horde')
        mobs.append('Goblin Horde')
    elif request_ == 'Tavern':
        mobs.append('Dragon')
        mobs.append('Dragon')
        mobs.append('Dragon')
        mobs.append('Dragon')
    # mobb = choice(mobs)
    return jsonify(mob=mobs)

 
