from marshmallow import Schema, fields
from .genre import GenreSchema
from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    favorite_genre = db.relationship("Genre")

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    surname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    # favorite_genre_id = fields.Int()
    favorite_genre = fields.Pluck(GenreSchema, "name")