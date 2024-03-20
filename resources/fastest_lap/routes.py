from flask import request

from app import app

from db import fastest_laps


@app.post('/fastestlaps')
def create_fastest_lap():
    data = request.get_json()
    print(data)
    fastest_laps[data['race']] = data
    return{
        'Fastest lap has been created successfully!' : fastest_laps[data['race']]
    }

@app.get('/fastestlaps')
def get_fastest_laps():
    try:
        return list(fastest_laps.values()), 200
    except:
        return {'message':"Failed to get fastest laps"}, 400

@app.put('/fastestlaps')
def update_fastest_lap():
    data = request.get_json()
    if data['race'] in fastest_laps:
        fastest_laps[data['race']] = data
        return {
            'Fastest lap updated successfully.' : fastest_laps[data['race']]
        }
    return {'error' : 'Race does not exist in the Database.'}, 400


@app.delete('/fastestlaps')
def delete_fastest_lap():
    data = request.get_json()
    if data['race'] in fastest_laps:
        del fastest_laps[data['race']]
        return {
            'The fastest lap has been deleted': f"{data['race']}'s fastest lap is no more. . . "
        }
    return {'error' : 'Race does not exist in the Database.'}, 400