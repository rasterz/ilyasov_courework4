from setup_db import db
from marshmallow import Schema, fields
from .director import DirectorSchema
from .genre import GenreSchema


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    genre = db.relationship("Genre")
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    # genre_id = fields.Int()
    genre = fields.Pluck(GenreSchema, "name")
    # director_id = fields.Int()
    director = fields.Pluck(DirectorSchema, "name")