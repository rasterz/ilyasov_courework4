from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one_by_id(self, uid):
        return self.session.query(User).get(uid)

    def get_one_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one_by_id(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one_by_id(user_d.get("id"))
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        user.favorite_genre_id = user_d.get("favorite_genre_id")

        self.session.add(user)
        self.session.commit()

    def change_password(self, user_d):
        user = self.get_one_by_id(user_d.get("id"))
        user.password = user_d.get("password")

        self.session.add(user)
        self.session.commit()