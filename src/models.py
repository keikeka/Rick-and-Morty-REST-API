from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    type = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    origin = db.Column(db.String(120), unique=False, nullable=False)
    location = db.Column(db.String(120), unique=False, nullable=False)
    image = db.Column(db.String(120), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Charater %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type": self.type,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image,
            "url": self.url,
            "created": self.created,
        }
        
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80), unique=False, nullable=False)
    dimension = db.Column(db.String(80), unique=False, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
  
    def __repr__(self):
        return '<Location %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "url": self.url,
            "created": self.created,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))    
    user = db.relationship("User", foreign_keys=[user_id])
    character = db.relationship('Character')
    location = db.relationship('Location')

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        location = None
        character = None
        if self.location is not None:
            location=self.location.serialize()
        if self.character is not None:
            character = self.character.serialize()
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "location_id": self.location_id,
        }
