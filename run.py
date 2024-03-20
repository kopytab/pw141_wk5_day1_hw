from app import app



@app.route('/')
def land():
    return{
        "Welcome to my page of the fastest Formula 1 laps and pit stops of 2024!" : "This page will show the stats of the top 10 fastest laps and pit stops of the 2024 season so far."
    }

