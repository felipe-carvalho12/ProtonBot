from lists import first_names, last_names
from random import randint


def get_id():
    _id_ = ''
    for i in range(0, 5):
        _id_ += str(randint(0, 9))
    return _id_


def get_name():
    return first_names[randint(0, len(first_names) - 1)]


def get_surname():
    return last_names[randint(0, len(last_names) - 1)]


def get_username(name, surname, id_):
    nm = name.lower().replace(' ', '')
    sn = surname.lower().replace(' ', '')
    return nm + sn + id_


def get_password(id_):
    return 'G3n3r@l' + id_


id_ = get_id()
name = get_name()
surname = get_surname()
username = get_username(name, surname, id_)
password = get_password(id_)
