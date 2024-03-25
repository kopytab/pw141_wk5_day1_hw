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