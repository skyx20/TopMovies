from app import db


class Movie(db.Model):
    __tablename__ = "Movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.Text, nullable=False)
