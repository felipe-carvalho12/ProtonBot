from new_user import get_username, get_password


class User:
    def __init__(self, id_, name, surname):
        self.id_ = id_
        self.name = name
        self.surname = surname
        self.username = get_username(self.name, self.surname, self.id_)
        self.password = get_password(self.id_)
        self.email = '{}@protonmail.com'.format(self.username)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
