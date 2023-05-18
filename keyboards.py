from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from queries import *


def generate_register_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_register = KeyboardButton(text="Register 📲")
    markup.row(btn_register)
    return markup


def generate_send_contact_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_send_contact = KeyboardButton(text="Send Contact 📲", request_contact=True)
    markup.row(btn_send_contact)
    return markup


def generate_submitting_user_data():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_yes = KeyboardButton(text="Yes ✅")
    btn_no = KeyboardButton(text="No ❌")
    markup.row(btn_yes, btn_no)
    return markup


def generate_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_menu = KeyboardButton(text='Menu 🍴')
    btn_orders = KeyboardButton(text='My Orders 🛍')
    btn_feedback = KeyboardButton(text='Feedback 📝')
    markup.add(btn_menu, btn_orders, btn_feedback)
    return markup


def generate_back_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_back = KeyboardButton(text="Back ⏮")
    markup.add(btn_back)
    return markup


def generate_for_locations():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_my_locations = KeyboardButton(text="🗺 My Locations")
    btn_geolocation = KeyboardButton(text="🌍 Send location", request_location=True)
    btn_back = KeyboardButton(text="Back ⏮")
    markup.row(btn_my_locations)
    markup.row(btn_geolocation, btn_back)
    return markup


def generate_confirm_location():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_yes = KeyboardButton(text="Yes ✅")
    btn_no = KeyboardButton(text="No ❌")
    btn_back = KeyboardButton(text="Back ⏮")
    markup.row(btn_yes, btn_no)
    markup.row(btn_back)
    return markup


def generate_categories_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    categories = get_all_categories()
    markup.add(*categories)
    btn_cart = KeyboardButton(text="Cart 🛒")
    btn_back = KeyboardButton(text="Back ⏮")
    markup.row(btn_cart, btn_back)
    return markup


def generate_user_addresses(telegram_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    user_addresses = get_user_addresses(telegram_id)
    markup.add(*user_addresses)
    btn_back = KeyboardButton(text="Back ⏮")
    markup.row(btn_back)
    return markup


def generate_category_products(category_name):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    products = get_category_products(category_name)
    buttons = []
    for product in products:
        btn = KeyboardButton(text=product)
        buttons.append(btn)

    markup.add(*buttons)
    return markup
