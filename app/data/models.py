
from app import db


class Suburb(db.Model):
    name = db.Column(db.String(100), nullable=False, primary_key=True)
    postcode = db.Column(db.Integer, nullable=False)
    lga = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer)
    median_age = db.Column(db.Integer)
    avg_household_size = db.Column(db.Float)
    num_uni_students = db.Column(db.Integer)
    median_weekly_rent = db.Column(db.Integer)
    num_houses = db.Column(db.Integer)
    num_apartments = db.Column(db.Integer)
    num_shared = db.Column(db.Integer)
    
    def __repr__(self) -> str:
        return f"Suburb('{self.name}', '{self.postcode}')"
