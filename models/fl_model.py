from app import f1db




class FL_Model(f1db.Model):

    __tablename__ = 'fastest laps'

    id = f1db.Column(f1db.Integer, primary_key = True)
    round = f1db.Column(f1db.Integer, nullable = False)
    race = f1db.Column(f1db.String(50), nullable = False)
    driver = f1db.Column(f1db.String(50), nullable = False)
    team = f1db.Column(f1db.String(50), nullable = False)
    time = f1db.Column(f1db.String(20), nullable = False)

    def save_fl(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_fl(self):
        f1db.session.delete(self)
        f1db.session.commit()


    def from_dict(self, fl_dict):
        for k, v in fl_dict.items():
            setattr(self, k, v)