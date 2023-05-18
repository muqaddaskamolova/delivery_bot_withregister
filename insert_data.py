import sqlite3

database = sqlite3.connect("mybot.db")
cursor = database.cursor()


def insert_categories():
    cursor.execute("""
    INSERT  INTO categories(category_name, category_image)
    VALUES ('Burger 🍔', 'images/category/burger_cat.jpg'),
     ('Pizza 🍕', 'images/category/pizza_cat.webp'), 
     ('Lavash 🫔', 'images/category/lavash.jpg'),
     ('Sandwich 🥪', 'images/category/sandwich_cat.jpg'), 
     ('Taco 🌮', 'images/category/taco_cat.jpg'),
     ('Hotdog 🌭', 'images/category/hotdog_cat.jpg'), 
     ('Chicken 🍗', 'images/category/chicken_cat.jpg'), 
     ('Fry Potato 🍟', 'images/category/frypotato_cat.jpg'),
     ('Drink 🥤', 'images/category/drink_cat.jpg'),
     ('Cake 🍰', 'images/category/cake_cat.jpg')
     """)


#insert_categories()

def insert_products_burger():
    cursor.execute("""
    INSERT INTO products(product_name,
                        product_description,
                        product_price,
                        product_image,
                        category_id)
    VALUES ('Hamburger 🍔',
    "A hamburger  is a food consisting of one or more cooked patties of ground meat, usually beef, placed inside 
    a sliced bread roll or bun. 
    The patty may be pan fried, grilled, smoked or flame broiled. Hamburgers are often served with cheese, lettuce, 
    tomato, onion, pickles, bacon, or chile, condiments such as ketchup, mustard, mayonnaise, relish, or special sauce
     and are frequently placed on sesame seed buns.",
    20000.00,
    'images/products/burger/hamburger.jpg',
    1),
    ('BiGburger 🍔',
   "A BiGburger  is a food consisting of one or more cooked patties of ground meat, usually beef, placed inside 
   a sliced bread roll or bun. The patty may be pan fried, grilled, smoked or flame broiled. Hamburgers are often served 
   with cheese, lettuce, tomato, onion, pickles, bacon, or chile, condiments such as ketchup, mustard, mayonnaise, 
   relish, or special sauce, and are frequently placed on sesame seed buns.",
    30000.00,
    'images/products/burger/bigburger.jpg',
    1), 
    ('Blackburger 🍔',
   "A Blackburger  is a food consisting of one or more cooked patties of ground meat, usually beef, placed inside 
   a sliced bread roll or bun. The patty may be pan fried, grilled, smoked or flame broiled. Hamburgers are often 
   served with cheese, lettuce, tomato, onion, pickles, bacon, or chile, condiments such as ketchup, mustard, 
   mayonnaise, relish, or special sauce, and are frequently placed on sesame seed buns.",
    40000.00,
    'images/products/burger/blackburger.jpg',
    1), 
     ('Chinaburger 🍔',
   "A Chinaburger  is a food consisting of one or more cooked patties of ground meat, usually beef, placed inside
    a sliced bread roll or bun. The patty may be pan fried, grilled, smoked or flame broiled. Hamburgers are often 
    served with cheese, lettuce, tomato, onion, pickles, bacon, or chile, condiments such as ketchup, mustard,
     mayonnaise, relish, or special sauce and are frequently placed on sesame seed buns.",
    50000.00,
    'images/products/burger/chinaburger.jpg',
    1)
    """)


insert_products_burger()
database.commit()
database.close()
