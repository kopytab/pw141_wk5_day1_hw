from flask import Flask, request

app = Flask(__name__)

pitstops = {
    1:{
        'position' : 1,
        'driver' : 'Charles Leclerc',
        'team' : 'Ferrari',
        'time' : '2.23 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    2:{
        'position' : 2,
        'driver' : 'Carlos Sainz',
        'team' : 'Ferrari',
        'time' : '2.27 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    3:{
        'position' : 3,
        'driver' : 'Max Verstappen',
        'team' : 'Red Bull',
        'time' : '2.27 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    4:{
        'position' : 4,
        'driver' : 'Sergio Perez',
        'team' : 'Red Bull',
        'time' : '2.29 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    5:{
        'position' : 5,
        'driver' : 'Lando Norris',
        'team' : 'McLaren',
        'time' : '2.33 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    6:{
        'position' : 6,
        'driver' : 'Yuki Tsunoda',
        'team' : 'RB',
        'time' : '2.34 Sec',
        'race' : 'Round 1 : Bahrain'
    },

    7:{
        'position' : 7,
        'driver' : 'Max Verstappen',
        'team' : 'Red Bull',
        'time' : '2.44 Sec',
        'race' : 'Round 2 : Saudi Arabia'
    },

    8:{
        'position' : 8,
        'driver' : 'Lewis Hamilton',
        'team' : 'Mercedes AMG',
        'time' : '2.51 Sec',
        'race' : 'Round 1 : Bahrain'
    },
    


    9:{
        'position' : 9,
        'driver' : 'Lewis Hamilton',
        'team' : 'Mercedes AMG',
        'time' : '2.51 Sec',
        'race' : 'Round 2 : Saudi Arabia'
    },

    10:{
        'position' : 10,
        'driver' : 'Kevin Magnussen',
        'team' : 'Hass',
        'time' : '2.56 Sec',
        'race' : 'Round 1 : Bahrain'
    }
}

@app.route('/')
def land():
    return{
        "Welcome to my page of the fastest Formula 1 pit stops of 2024!" : "This page will show the stats of the top 10 fastest pit stops of the 2024 season so far."
    }

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