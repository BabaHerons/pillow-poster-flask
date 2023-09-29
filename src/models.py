from src import db

class Image(db.Model):
    __tablename__= "image"
    id = db.Column(db.String(100), primary_key=True , nullable=False, unique=True)
    image = db.Column(db.LargeBinary(), nullable=False)

class BackgroundImage(db.Model):
    __tablename__= "background_image"
    id = db.Column(db.Integer(), primary_key=True , nullable=False, unique=True)
    image = db.Column(db.LargeBinary(), nullable=False)