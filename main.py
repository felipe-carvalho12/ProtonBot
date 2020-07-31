from new_user import get_id, get_name, get_surname
from Classes import User
from form_Proton import get_email
from form_Twitter import get_twitter_accounts


accounts_number = int(input('Número de contas: '))
users_created = []

for i in range(0, accounts_number):
    user = User(get_id(), get_name(), get_surname())

    get_email(user.username, user.password)
    get_twitter_accounts(user.username, user.email)

    print(user)
