from repositories.UsersRepository import UsersRepository
from app import app


class UsersService(object):
    def __init__(self):
        self.users_repository = UsersRepository()

    def login(self,
              username,
              password):
        return self.users_repository.login(username,
                                           password)

    def get_user_by_id(self, id):
        return self.users_repository.get_user_by_id(id)

    def get_user_by_name(self, name):
        return self.users_repository.get_user_by_name(name)
    
    def get_all_users(self):
        return self.users_repository.get_all_users()
    
    def crear_nuevo_usuario(self, email, name, password, username):
        return self.users_repository.crear_nuevo_usuario(email, name, password, username)