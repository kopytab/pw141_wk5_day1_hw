from flask import request

from app import app

from db import pitstops

@app.route('/pitstops')
def pit_page():
    return{
        'pitstops' : list(pitstops.values())
    
    }

@app.route('/pitstops', methods = ['POST'])
def create_pitstop():
    data = request.get_json()
    print(data)
    pitstops[data['position']] = data
    return{
        'Pitstop has been created successfully!' : pitstops[data['position']]
    }

@app.get('/pitstops')
def get_pitstops():
    try:
        return list(pitstops.values()), 200
    except:
        return {'message':"Failed to get pitstops"}, 400

@app.route('/pitstops', methods=["PUT"])
def update_pitstop():
    data = request.get_json()
    if data['position'] in pitstops:
        pitstops[data['position']] = data
        return {
            'Pitstop updated successfully.' : pitstops[data['position']]
        }
    return {
        'error' : 'Position out of range(1-10)'
    }


@app.route('/pitstops', methods=["DELETE"])
def delete_pitstop():
    data = request.get_json()
    if data['position'] in pitstops:
        del pitstops[data['position']]
        return {
            'The pitstop has been deleted': f"{data['driver']}'s pitstop is no more. . . "
        }