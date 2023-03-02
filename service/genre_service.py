from dao.genre_dao import GenreDAO

class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def get_one_by_id(self, gid: int):
        return self.dao.get_one_by_id(gid)

    # def create(self, genre_d):
    #     return self.dao.create(genre_d)
    #
    # def update(self, genre_d):
    #     self.dao.update(genre_d)
    #     return self.dao
    #
    # def delete(self, gid):
    #     self.dao.delete(gid)