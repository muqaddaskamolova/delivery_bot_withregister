import sqlite3

database = sqlite3.connect("mybot.db")
cursor = database.cursor()


def create_users_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER BIGINT UNIQUE ,
    full_name TEXT,
    age TEXT,
    contact TEXT
    )
    """)


#create_users_table()


def create_locations_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations(
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    loc_latitude TEXT,
    loc_longitude TEXT,
    location_name TEXT UNIQUE) 
    """)


#create_locations_table()


def create_categories_table():
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS categories(
       category_id INTEGER PRIMARY KEY AUTOINCREMENT,
       category_name TEXT UNIQUE,
        category_image TEXT)
       """)


#create_categories_table()


def create_product_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    product_description TEXT,
    product_price DECIMAL(6, 2),
    product_image TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
    )
    """)


#create_product_table()
database.commit()
database.close()
# database
