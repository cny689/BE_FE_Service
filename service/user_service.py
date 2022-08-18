from model.user_dao import UserDao


class UserService:
    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config = config

    def create_new_user(self, new_user):
        user = self.user_dao.insert_user(new_user)
        return user