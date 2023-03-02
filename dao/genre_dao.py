from .model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self, filters):
        page = filters.get('page')
        stmt = self.session.query(Genre)
        if page is not None:
            stmt = stmt.paginate(page=page, per_page=12).items
        return stmt

    def get_one_by_id(self, gid: int):
        return self.session.query(Genre).get(gid)

    # def create(self, genre_d):
    #     ent = Genre(**genre_d)
    #     self.session.add(ent)
    #     self.session.commit()
    #     return ent
    #
    # def delete(self, did):
    #     genre = self.get_one_by_id(did)
    #     self.session.delete(genre)
    #     self.session.commit()
    #
    # def update(self, genre_d):
    #     genre = self.get_one_by_id(genre_d.get("id"))
    #     genre.name = genre_d.get("name")
    #
    #     self.session.add(genre)
    #     self.session.commit()