from data import load_data, save_data, remove_file
from user import User


class Security:
    USERS = "users"
    user_login = ''

    def __init__(self):
        self.user_login = ''

    def is_user_login(self):
        if self.user_login == '':
            return False
        return True

    def is_admin(self):
        if self.is_user_login() and self.user_login == 'admin':
            return True
        return False

    def login(self, user, password):
        users = load_data(self.USERS)
        for u in users:
            if u.name == user and u.password == password:
                self.user_login = u.name
                return True
        return False

    def logout(self):
        self.user_login = ''

    def create(self, name, password):
        if name == 'users':
            return False
        users = load_data(self.USERS)
        if len(users) > 0:
            for u in users:
                if u.name == name:
                    return False
        user = User(name, password)
        users.append(user)
        save_data(self.USERS, users)
        return True

    def create_admin(self):
        self.create('admin', 'admin')

    def remove(self, user):
        if user != 'admin':
            users = load_data(self.USERS)
            for index, u in enumerate(users, start=0):
                if u.name == user:
                    del users[index]
                    save_data(self.USERS, users)
                    remove_file(user)
                    return True
            return False

    def draw(self):
        users = load_data(self.USERS)
        for c in users:
            print(c.name, "-", c.password)
