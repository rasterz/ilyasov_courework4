from dao.favorite_dao import FavoriteDAO

class FavoriteService:

    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_one_by_user_and_movie(self, favorite_d):
        return self.dao.get_one_by_user_and_movie(favorite_d)


    def add(self, favorite_d):
        return self.dao.add(favorite_d)

    def delete(self, favorite_d):
        self.dao.delete(favorite_d)