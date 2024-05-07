from app import f1db


class Ci_Model(f1db.Model):

    __tablename__ = 'constructor info'

    id = f1db.Column(f1db.Integer, primary_key = True)
    fullname = f1db.Column(f1db.String(50), nullable = False)
    driver1 = f1db.Column(f1db.String(50), nullable = False)
    driver2 = f1db.Column(f1db.String(50), nullable = False)
    teamcheif = f1db.Column(f1db.String(50), nullable = False)
    base = f1db.Column(f1db.String(50), nullable = False)
    firstentry = f1db.Column(f1db.String(50), nullable = False)
    championships = f1db.Column(f1db.String(50), nullable = False)
    
    

    def save_ci(self):
        f1db.session.add(self)
        f1db.session.commit()

    def del_ci(self):
        f1db.session.delete(self)
        f1db.session.commit()

    def from_dict(self, ci_dict):
        for k, v in ci_dict.items():
            setattr(self, k, v)