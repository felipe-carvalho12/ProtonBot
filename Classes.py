class User:
    def __init__(self, id_, name, surname, username, password):
        self.id = id_
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password

    def get_email(self):
        return '{}@protonmail.com'.format(self.username)
