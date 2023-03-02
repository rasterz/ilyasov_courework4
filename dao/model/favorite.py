from setup_db import db
from marshmallow import Schema, fields
from .user import UserSchema
from .movie import MovieSchema


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie = db.relationship("Movie")
    user = db.relationship("User")


class FavoriteSchema(Schema):
    id = fields.Int(dump_only=True)
    movie = fields.Pluck(MovieSchema, "title")
    user = fields.Pluck(UserSchema, "email")