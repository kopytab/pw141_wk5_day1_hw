from app import f1db


class Sched_Model(f1db.Model):

    __tablename__ = 'schedule'

    id = f1db.Column(f1db.Integer, primary_key = True)
    round = f1db.Column(f1db.String(50), nullable = False)
    circuit = f1db.Column(f1db.String(50), nullable = False)
    racename = f1db.Column(f1db.String(50), nullable = False)
    country = f1db.Column(f1db.String(50), nullable = False)
    datespan = f1db.Column(f1db.String(50), nullable = False)
    fp1 = f1db.Column(f1db.String(50), nullable = False)
    fp2 = f1db.Column(f1db.String(50), nullable = True)
    fp3 = f1db.Column(f1db.String(50), nullable = True)
    qual = f1db.Column(f1db.String(50), nullable = False)
    race = f1db.Column(f1db.String(50), nullable = False)
    sprint_qual= f1db.Column(f1db.String(50), nullable = True)
    sprint_race = f1db.Column(f1db.String(50), nullable = True)

    def save_sched(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_sched(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, sched_dict):
        for k, v in sched_dict.items():
            setattr(self, k, v)