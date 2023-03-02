from .model.favorite import Favorite
from helpers.exceptions import NoResultFound


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        user_id = filters.get('user_id')
        stmt = self.session.query(Favorite)
        if user_id is not None:
            stmt = stmt.filter(Favorite.user_id == user_id)
        return stmt.all()

    def get_one_by_user_and_movie(self, favorite_d):
        try:
            return self.session.query(Favorite).filter(
                Favorite.user_id == favorite_d['user_id'],
                Favorite.movie_id == favorite_d['movie_id']
            ).one()
        except NoResultFound:
            return None


    def add(self, favorite_d):
        ent = Favorite(**favorite_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, favorite_d):
        favorite = self.get_one_by_user_and_movie(favorite_d)
        self.session.delete(favorite)
        self.session.commit()