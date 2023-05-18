import sqlite3
from insert_data import *


def insert_user(telegram_id, full_name, age, contact):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO users(telegram_id, full_name, age, contact)
    VALUES (?, ?, ?, ?) ''', (telegram_id, full_name, age, contact))

    database.commit()
    database.close()


def get_all_users():
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()
    cursor.execute("""
    SELECT telegram_id FROM users;
    """, )
    users = cursor.fetchall()
    users_tg_ids = []

    for user in users:
        users_tg_ids.append(user[0])
    database.close()

    return users_tg_ids


def get_user_data(telegram_id):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute("""
       SELECT * FROM users
       WHERE telegram_id = ?
       """, (telegram_id,))

    user_data = cursor.fetchone()
    database.close()
    return user_data


def insert_location(telegram_id, latitude, longitude, location_name):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
      INSERT OR IGNORE INTO locations(telegram_id, loc_latitude,loc_longitude,location_name)
      VALUES (?, ?, ?, ?) ''', (telegram_id, latitude, longitude, location_name))

    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
        SELECT category_name FROM categories;
          ''')
    categories = cursor.fetchall()
    categories_list = []

    for c in categories:
        categories_list.append(c[0])

    database.close()
    return categories_list


def get_user_addresses(telegram_id):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
        SELECT location_name FROM locations
        WHERE telegram_id = ?
          ''', (telegram_id,))
    user_addresses = cursor.fetchall()
    user_addresses_list = []

    for u in user_addresses:
        user_addresses_list.append(u[0])

    database.close()
    return user_addresses_list


def get_category_image(category_name):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
          SELECT category_image FROM categories
          WHERE category_name = ?
            ''', (category_name,))
    category_image = cursor.fetchone()[0]
    database.close()
    return category_image


def get_category_products(category_name):
    database = sqlite3.connect("mybot.db")
    cursor = database.cursor()

    cursor.execute('''
    SELECT category_id FROM categories
     WHERE category_name = ?
     ''', (category_name,))
    category_id = cursor.fetchone()[0]

    cursor.execute('''
    SELECT product_name FROM products
    WHERE category_id = ?
     ''', (category_id,))

    products_name = cursor.fetchall()
    database.close()
    products = []
    for product in products_name:
        products.append(product[0])

    return products
