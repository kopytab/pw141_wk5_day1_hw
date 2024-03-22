from marshmallow import Schema, fields

class Fastest_lapSchema(Schema):
    round = fields.Int(required=True )
    race = fields.Str(required=True)
    driver = fields.Str(required=True)
    team = fields.Str(required=True)
    time = fields.Str(required=True)
class PitstopsSchema(Schema):
    
    position = fields.Int(required=True)
    driver = fields.Str(required=True)
    race = fields.Str(required=True)
    team = fields.Str(required=True)
    time = fields.Str(required=True)