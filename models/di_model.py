from app import f1db


class Di_Model(f1db.Model):

    __tablename__ = 'driver info'

    id = f1db.Column(f1db.Integer, primary_key = True)
    number = f1db.Column(f1db.String(50), nullable = False)
    driver = f1db.Column(f1db.String(50), nullable = False)
    nationality = f1db.Column(f1db.String(50), nullable = False)
    team = f1db.Column(f1db.String(50), nullable = False)
    dob = f1db.Column(f1db.String(50), nullable = False)
    

    def save_di(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_di(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, di_dict):
        for k, v in di_dict.items():
            setattr(self, k, v)