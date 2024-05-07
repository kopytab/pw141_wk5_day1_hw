from app import f1db


class Ds_Model(f1db.Model):

    __tablename__ = 'driver standings'

    id = f1db.Column(f1db.Integer, primary_key = True)
    position = f1db.Column(f1db.String(50), nullable = False)
    driver = f1db.Column(f1db.String(50), nullable = False)
    nationality = f1db.Column(f1db.String(50), nullable = False)
    team = f1db.Column(f1db.String(50), nullable = False)
    points = f1db.Column(f1db.String(50), nullable = False)
    

    def save_ds(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_ds(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, ds_dict):
        for k, v in ds_dict.items():
            setattr(self, k, v)