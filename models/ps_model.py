from app import f1db


class PS_Model(f1db.Model):

    __tablename__ = 'pit stops'

    id = f1db.Column(f1db.Integer, primary_key = True)
    position = f1db.Column(f1db.Integer, nullable = False)
    driver = f1db.Column(f1db.String(50), nullable = False)
    race = f1db.Column(f1db.String(50), nullable = False)
    team = f1db.Column(f1db.String(50), nullable = False)
    time = f1db.Column(f1db.String(20), nullable = False)

    def save_ps(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_ps(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, ps_dict):
        for k, v in ps_dict.items():
            setattr(self, k, v)