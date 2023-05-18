from telebot import TeleBot
from telebot.types import Message, CallbackQuery, ReplyKeyboardRemove
from configs import *
from keyboards import *
from queries import *
from locations import *

bot = TeleBot(TOKEN, parse_mode='HTML')
users_data = {}


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    user_id = message.from_user.id
    users = get_all_users()

    if user_id in users:
        main_menu(message)
    else:
        bot.send_message(user_id, f"""Hello, dear user"""
                                  f""" Please, register to use the bot!""",
                         reply_markup=generate_register_btn())


@bot.message_handler(func=lambda message: message.text == "Register 📲")
def ask_full_name(message: Message):
    global users_data
    user_id = message.from_user.id
    users_data[user_id] = {
        "user_id": user_id
    }
    print(users_data)
    msg = bot.send_message(user_id, "Enter your name and surname:",
                           reply_markup=ReplyKeyboardRemove())

    bot.register_next_step_handler(msg, ask_age)


def ask_age(message: Message):
    global users_data
    user_id = message.from_user.id
    full_name = message.text
    users_data[user_id].update({
        "full_name": full_name
    })
    print(users_data)
    msg = bot.send_message(user_id, "Enter your age:")

    bot.register_next_step_handler(msg, ask_contact)


def ask_contact(message: Message):
    global users_data
    user_id = message.from_user.id
    age = message.text
    users_data[user_id].update({
        "age": age
    })
    print(users_data)
    msg = bot.send_message(user_id, "Enter your contact:",
                           reply_markup=generate_send_contact_btn())
    bot.register_next_step_handler(msg, show_register_data)


def show_register_data(message: Message):
    global users_data
    user_id = message.from_user.id
    if message.content_type == "contact":
        contact = message.contact.phone_number
        users_data[user_id].update({
            "contact": contact
        })

    elif message.content_type == "text":
        contact = message.text
        users_data[user_id].update({
            "contact": contact
        })
    print(users_data)
    msg = bot.send_message(user_id,
                           f"""<b>Name and Surname:</b><i>{users_data[user_id]['full_name']}</i><b>Age:</b><i>{users_data[user_id]['age']}</i><b>Phone number:</b><i>{users_data[user_id]['contact']}</i>""",
                           reply_markup=generate_submitting_user_data())

    bot.register_next_step_handler(msg, submit_unsubmit)


def submit_unsubmit(message: Message):
    global users_data
    user_id = message.from_user.id
    if message.text == "Yes ✅":
        insert_user(telegram_id=user_id,
                    full_name=users_data[user_id]['full_name'],
                    age=users_data[user_id]['age'],
                    contact=users_data[user_id]['contact'], )
        users_data.pop(user_id)
        bot.send_message(user_id, """You have successfully submitted! 🥳🥳🥳""",
                         reply_markup=ReplyKeyboardRemove())
        main_menu(message)
    elif message.text == "No ❌":
        users_data.pop(user_id)
        command_start(message)


# main menu
def main_menu(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"""Please, choose one of the following""",
                     reply_markup=generate_main_menu())


# Menu
@bot.message_handler(func=lambda message: message.text == 'Menu 🍴')
def ask_location(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f"""Please,  Send your location📍 or choose your address👇!""",
                           reply_markup=generate_for_locations())
    bot.register_next_step_handler(msg, submit_location)


def submit_location(message: Message):
    chat_id = message.chat.id
    if message.text == "🗺 My Locations":
        my_addresses(message)
    elif message.content_type == 'location':
        latitude = message.location.latitude
        longitude = message.location.longitude
        location_name = get_loc_name(latitude=latitude, longitude=longitude)

        msg = bot.send_message(chat_id, f"""Address where you want to order:{location_name}\n
Are you confirm your location?\n""", reply_markup=generate_confirm_location())
        bot.register_next_step_handler(msg, submitting_location, latitude, longitude, location_name)

    elif message.text == "Back ⏮":
        main_menu(message)


def submitting_location(message: Message, latitude, longitude, location_name):
    chat_id = message.chat.id
    if message.text == "Yes ✅":
        insert_location(telegram_id=chat_id, latitude=latitude, longitude=longitude, location_name=str(location_name))

        show_categories_menu(message)
    elif message.text == "No ❌":
        ask_location(message)
    elif message.text == "Back ⏮":
        ask_location(message)


def my_addresses(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Please choose one of these Shipping Address!",
                           reply_markup=generate_user_addresses(chat_id))

    bot.register_next_step_handler(msg, show_categories_menu)


def show_categories_menu(message: Message):
    chat_id = message.chat.id
    if message.text == "Back ⏮":
        ask_location(message)
    bot.send_message(chat_id, "Please, Choose category 👀", reply_markup=generate_categories_menu())


CATEGORIES = get_all_categories()


@bot.message_handler(func=lambda message: message.text in CATEGORIES)
def show_category_products(message: Message):
    chat_id = message.chat.id
    category_name = message.text
    category_image = get_category_image(category_name)
    bot.send_message(chat_id, f"Choose one of the following:")
    with open(category_image, mode='rb') as img:
        bot.send_photo(chat_id, photo=img, caption=f"You have chosen {category_name} category!",
                       reply_markup=generate_category_products(category_name))

    # Feedback


@bot.message_handler(func=lambda message: message.text == 'Feedback 📝')
def ask_feedback(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f"""Send your feedback!""", reply_markup=generate_back_button())
    bot.register_next_step_handler(msg, thanks_for_feedback)


def thanks_for_feedback(message: Message):
    chat_id = message.chat.id

    if message == "Back ⏮":
        main_menu(message)
    else:
        feedback = message.text
        user_data = get_user_data(chat_id)
    bot.send_message(CHANNEL_FEEDBACK_ID, f"""Name, Surname: {user_data[2]} 
    Contact number: {user_data[4]}
    Feedback: {feedback}""")

    bot.send_message(chat_id, f"""Thanks your feedback!😍😍😍""")
    main_menu(message)


bot.polling(none_stop=True)
