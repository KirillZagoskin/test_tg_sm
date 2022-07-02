import os
import sqlite3

conn = sqlite3.connect('/Users/kirillzagoskin/code/sreda.today/app/sredaengine/db.sqlite3')
cursor = conn.cursor()


def check_user_and_get_link(tg_id):
    cursor.execute(f'SELECT username, link FROM users_user WHERE tg_id = {tg_id}')
    result = cursor.fetchone()
    if result:
        username, link = result
        return username, link
    else:
        return None, None


def insert_user(id, username, link, datetime_now):
    columns = 'tg_id,username,link,password,is_superuser,first_name,last_name,email,is_staff,is_active,date_joined'
    values = (id, username, link, 'NULL', 0, 'NULL', 'NULL', 'NULL', 0, 1, datetime_now)
    sql = f''' INSERT INTO users_user({columns})
              VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
    cursor.execute(sql, values)
    conn.commit()
