from app import f1db


class Cs_Model(f1db.Model):

    __tablename__ = 'constructor standings'

    id = f1db.Column(f1db.Integer, primary_key = True)
    position = f1db.Column(f1db.String(50), nullable = False)
    team = f1db.Column(f1db.String(50), nullable = False)
    points = f1db.Column(f1db.String(50), nullable = False)
    

    def save_cs(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_cs(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, cs_dict):
        for k, v in cs_dict.items():
            setattr(self, k, v)