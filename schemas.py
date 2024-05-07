from marshmallow import Schema, fields

class Fastest_lapSchema(Schema):

    id = fields.Str(dump_only=True)
    round = fields.Int(required=True )
    race = fields.Str(required=True)
    driver = fields.Str(required=True)
    team = fields.Str(required=True)
    time = fields.Str(required=True)

class PitstopsSchema(Schema):
    
    id = fields.Str(dump_only=True)
    position = fields.Int(required=True)
    driver = fields.Str(required=True)
    race = fields.Str(required=True)
    team = fields.Str(required=True)
    time = fields.Str(required=True)

class ConstructorStandingsSchema(Schema):
    id = fields.Str(dump_only=True)
    position = fields.Str(required=True)
    team = fields.Str(required=True)
    points = fields.Str(required=True)

class DriverStandingsSchema(Schema):
    id = fields.Str(dump_only=True)
    position = fields.Str(required=True)
    driver = fields.Str(required=True)
    nationality = fields.Str(required=True)
    team = fields.Str(required=True)
    points = fields.Str(required=True)

class DriverInfoSchema(Schema):
    id = fields.Str(dump_only=True)
    number = fields.Str(required=True)
    driver = fields.Str(required=True)
    nationality = fields.Str(required=True)
    team = fields.Str(required=True)
    dob = fields.Str(required=True)

class ConstructorInfoSchema(Schema):
    id = fields.Str(dump_only=True)
    fullname = fields.Str(required=True)
    driver1 = fields.Str(required=True)
    driver2 = fields.Str(required=True)
    teamcheif = fields.Str(required=True)
    base = fields.Str(required=True)
    firstentry = fields.Str(required=True)
    championships = fields.Str(required=True)

class ScheduleSchema(Schema):
    id = fields.Str(dump_only=True)
    round = fields.Str(required=True)
    circuit = fields.Str(required=True)
    racename = fields.Str(required=True)
    country = fields.Str(required=True)
    datespan = fields.Str(required=True)
    fp1 = fields.Str(required=True)
    fp2 = fields.Str(required=False)
    fp3 = fields.Str(required=False)
    qual = fields.Str(required=True)
    race = fields.Str(required=True)
    sprint_qual = fields.Str(required=False)
    sprint_race = fields.Str(required=False)