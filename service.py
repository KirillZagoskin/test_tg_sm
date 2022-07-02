from datetime import datetime
import string
import random
from unittest import result

from db import check_user_and_get_link, insert_user


SITE_NAME = 'http://127.0.0.1:8000/users/'

def _create_link_and_insert_to_db(user_id, username):
    datetime_now = datetime.now()
    letters = string.digits + string.ascii_letters
    link = ''.join(random.choice(letters) for i in range(10))
    insert_user(user_id, username, link, datetime_now)
    return  SITE_NAME + link



def send_message(user_id, username):
    if username == None:
        return 'Нужен username'
    username_db, link = check_user_and_get_link(user_id)

    if username_db and link:
        if username_db == username:
            return 'Чтобы пройти регистрацию, пройдите по этой ссылке:\n\n' + SITE_NAME + link
        else:
            return f'При регистрации ваш username был - {username_db}, он и будет сохранен, когда вы завершите регистрацию.\n\nСделать это можно по этой ссылке:\n\n' + SITE_NAME + link
    elif username_db is None:
        return f'Привет! Для регистрации нужно пройти по этой ссылке:\n\n{_create_link_and_insert_to_db(user_id, username)}'
    else:
        return'Вы уже зарегистрировались!'

