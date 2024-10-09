import telebot
from telebot import types
from keep_alive import keep_alive

API_TOKEN = '7857970440:AAG7D4Uawz14-HFnBQzYb7uOYAaZPl0NNuA'

bot = telebot.TeleBot(API_TOKEN)

# Dictionary to store the menu for each day and meal type
menus = {
    "monday": {
        "breakfast": {
            "menu": "🍞 Pav Bhaji, ☕ Tea",
            "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/pav-bhaji-1.jpg"
        },
        "lunch": {
            "menu": "🥗 Mix Veg, 🍛 Dal Fry, 🍚 Green Peas Pulao, 🥣 Raita, 🫓 Chapati, 🍎 Fruits",
            "image": "https://preview.redd.it/veg-thali-rajma-masala-masoor-dal-mattar-pulao-palak-raita-v0-7x702xtcy8ja1.jpg?width=1080&crop=smart&auto=webp&s=632bcc0b6ab1c6047d9d061f863368a658ccfb2a"
        },
        "snacks": {
            "menu": "🍞 Masala Pav, ☕ Tea",
            "image": "https://madhurasrecipe.com/wp-content/uploads/2020/10/Masala-Pav-Marathi-Recipe.jpg"
        },
        "dinner": {
            "menu": "🍲 Matar Paneer/ Palak Paneer, 🍛 Black Dal, 🍚 Plain Rice, 🍮 Shahi Tukda, 🫓 Chapati",
            "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/matar-paneer-0.jpg"
        }
    },
    "tuesday": {
        "breakfast": {
            "menu": "🥣 Poha, 🥘 Black Chana/ Dalia, 🌰 Coconut Chutney, ☕ Coffee",
            "image": "https://media.vogue.in/wp-content/uploads/2020/10/poha-recipe-1920x1080.jpg"
        },
        "lunch": {
            "menu": "🍛 Rajma Masala, 🥔 Aloo Bhindi Dry, 🍚 Plain Rice, 🥣 Curd, 🥗 Salad, 🫓 Chapati, 🍇 Fruits",
            "image": "https://www.secondrecipe.com/wp-content/uploads/2017/08/rajma-chawal-1-720x551.jpg"
        },
        "snacks": {
            "menu": "🥟 Samosa, 🌶️ Chutney, ☕ Tea",
            "image": "https://www.awesomecuisine.com/wp-content/uploads/2014/11/vegetable-samosa.jpg"
        },
        "dinner": {
            "menu": "🍲 Chhole Masala, 🍛 Dal Fry, 🍚 Masala Rice, 🫓 Methi Roti, 🍨 Sheera",
            "image": "https://pipingpotcurry.com/wp-content/uploads/2017/05/Instant-Pot-Chana-Masala.-Chole.-Chickpeas.jpg"
        }
    },
    "wednesday": {
        "breakfast": {
            "menu": "🥞 Idli, 🍲 Sambhar/ 🌰 Coconut Chutney, ☕ Tea",
            "image": "https://vaya.in/recipes/wp-content/uploads/2018/02/Idli-and-Sambar-1.jpg"
        },
        "lunch": {
            "menu": "🍛 Dal Makhni, 🥗 Chana Cabbage Dry, 🍚 Zeera Rice, 🥣 Curd, 🫓 Chapati, 🍎 Fruits",
            "image": "https://www.cookwithmanali.com/wp-content/uploads/2019/04/Restaurant-Style-Dal-Makhani.jpg"
        },
        "snacks": {
            "menu": "🍔 Vada Pav, ☕ Tea",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYPjqgA4mp3J-T5DBx6oucBYC5v_WligkX8w&s"
        },
        "dinner": {
            "menu": "🍲 Paneer Kofta/ Chicken Curry, 🍛 Dal Fry, 🍚 Rice, 🫓 Chapati, 🍮 Fruit Custard",
            "image": "https://cdn3.foodviva.com/static-content/food-images/curry-recipes/paneer-kofta-recipe/paneer-kofta-recipe.jpg"
        }
    },
    "thursday": {
        "breakfast": {
            "menu": "🥘 Puri Bhaji, ☕ Tea",
            "image": "https://maayeka.com/wp-content/uploads/2014/07/poori-bhaji-aloo-tamatar-sabzi.jpg"
        },
        "lunch": {
            "menu": "🍚 Veg Biryani, 🍲 Curry, 🍘 Papad, 🥣 Raita, 🍇 Fruits",
            "image": "https://theartisticcook.com/wp-content/uploads/2024/01/Vegetablebiryani1.jpg"
        },
        "snacks": {
            "menu": "🥣 Poha, 🌶️ Chutney, ☕ Coffee",
            "image": "https://media.vogue.in/wp-content/uploads/2020/10/poha-recipe-1920x1080.jpg"
        },
        "dinner": {
            "menu": "🥔 Aloo Gobhi/ Veg Tawa, 🍛 Chana Dal Palak, 🍚 Zeera Rice, 🫓 Ajwain Chapati, 🍩 Gulab Jamun",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrEhyeJ7g4kKXTqwY5oF14ryu3pmLNiiBg5A&s"
        }
    },
    "friday": {
        "breakfast": {
            "menu": "🍞 Bread Butter Jam, 🥘 Veg Cutlet/ 🥚 Boiled Eggs, ☕ Tea",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKAVql9OeIiznXgM5DVVbrt_ffBQkwObq5Tw&s"
        },
        "lunch": {
            "menu": "🥔 Aloo Matar, 🥣 Dahi Kadhi, 🧅 Onion Pakoda, 🍚 Plain Rice, 🥗 Salad, 🫓 Roti, 🍎 Fruits",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7bo36uK3-WAigkTIpM9qTLk0J6e4fKSanKA&s"
        },
        "snacks": {
            "menu": "🍞 Bread Pakoda, 🌶️ Chutney, ☕ Tea",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtO9oQyHjXVgCWUkZY-VdIoMjFht5Ep-T6GQ&s"
        },
        "dinner": {
            "menu": "🍲 Paneer Kadai/ 🍳 Egg Curry, 🍚 Plain Rice, 🍛 Dal Fry, 🫓 Chapati, 🍮 Shevai Kheer",
            "image": "https://www.funfoodfrolic.com/wp-content/uploads/2020/12/Kadhai-Paneer-Thumbnail.jpg"
        }
    },
    "saturday": {
        "breakfast": {
            "menu": "🥔 Aloo Paratha, 🥣 Curd, ☕ Tea",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL0Zq6X0Ih5ODzljjrNF4CqOmXIDazdidGSA&s"
        },
        "lunch": {
            "menu": "🫓 Methi Roti/ 🍛 Chhole Bhature, 🍲 Chhole Masala, 🍚 Rice, 🍛 Dal Fry, 🥣 Boondi Raita, 🥗 Salad, 🍎 Fruits",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSHuqEQvNy--dkfLm4j4WW74dgvb2tb4HilQ&s"
        },
        "snacks": {
            "menu": "🍲 Bhel (Onion+Chilies incl.), ☕ Coffee",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj3fb1raHsOqjESFwLP_P5wVEGg5gi1Cb6dg&s"
        },
        "dinner": {
            "menu": "🍲 Soyabean Sabzi, 🍛 Masoor Dal Fry, 🍚 Masala Rice, 🫓 Chapati, 🍮 Rice Kheer/ 🍜 Chinese Food",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgXRbxDjMPkdfsE1It1wcf7fEqRw5x_yUHmA&s"
        }
    },
    "sunday": {
        "breakfast": {
            "menu": "🍅 Onion-Tomato Uttapam/ 🍲 Veg Upma, 🍲 Sambhar, ☕ Tea",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGf8TNraePqjNMbzCCyxlqaQJmkMquUfbicA&s"
        },
        "lunch": {
            "menu": "🍛 Black Chana Masala, 🍛 Dal Fry, 🍚 Rice, 🥣 Raita, 🫓 Chapati, 🍇 Fruits",
            "image": "https://www.indianveggiedelight.com/wp-content/uploads/2023/01/kala-chana-curry-recipe-featured.jpg"
        },
        "snacks": {
            "menu": "🍞 Cream Bun, ☕ Tea",
            "image": "https://www.bigbasket.com/media/uploads/p/l/60000891_2-fresho-cream-bun-vanilla-flavour-freshly-baked.jpg"
        },
        "dinner": {
            "menu": "🥔 Aloo Palak/ Aloo Matar, 🍲 Pancharatna Dal, 🍚 Green Peas Pulav, 🫓 Puri/ Methi Roti, 🍮 Sabudana Kheer",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgUeMaMBhP9QCn7mo8gtCSlLyKkuCW3vQpWQ&s"
        }
    }
}


@bot.message_handler(commands=['help'])
def help_user(message):
    help_text = """
    Here are the commands you can use:
    /start - Start selecting the day and meal
    /help - To check for all commands in this bot
    /weekly_menu - Get the full week's menu
    """
    bot.send_message(message.chat.id, help_text)


# Global variables to store user progress
user_states = {}  # To store the current step for each user
STEP_DAY_SELECTION = "day_selection"
STEP_MEAL_SELECTION = "meal_selection"


# Start and day selection
@bot.message_handler(commands=['start'])
def greet_user(message):

    global user_states
    user_states[
        message.chat.
        id] = STEP_DAY_SELECTION  # Set the current state to day selection
    bot.send_message(
        message.chat.id,
        "👋 Welcome to the Mess Menu Bot! You can explore the menu for the week.\nUse /help for more commands."
    )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       resize_keyboard=True)
    days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    for day in days:
        markup.add(day)

    bot.send_message(message.chat.id,
                     "Please select a day of the week:",
                     reply_markup=markup)


@bot.message_handler(commands=['weekly_menu'])
def send_weekly_menu(message):
    for day, meals in menus.items():
        bot.send_message(message.chat.id, f"📅 {day.capitalize()}:\n")
        for meal, data in meals.items():
            bot.send_message(message.chat.id,
                             f"{meal.capitalize()}: {data['menu']}")


# Handle day selection
@bot.message_handler(func=lambda message: message.text.lower() in [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
])
def select_meal_type(message):
    global user_states
    user_states[
        message.chat.
        id] = STEP_MEAL_SELECTION  # Set the current state to meal selection

    current_day = message.text.lower()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       resize_keyboard=True)
    meals = ['Breakfast', 'Lunch', 'Snacks', 'Dinner', 'Back']
    for meal in meals:
        markup.add(meal)

    bot.send_message(
        message.chat.id,
        f"You've selected {current_day.capitalize()}. Now, please select the type of meal.",
        reply_markup=markup)

    # Store selected day for menu retrieval
    bot.register_next_step_handler(message, show_menu, current_day)


# Show menu or navigate back
def show_menu(message, current_day):
    meal_type = message.text.lower()

    if meal_type == "back":
        # If the user presses Back, return to the day selection
        select_meal_type(message)
    elif meal_type in ['breakfast', 'lunch', 'snacks', 'dinner']:
        menu_info = menus.get(current_day, {}).get(meal_type, None)

        if menu_info:
            # Send menu text
            menu_text = menu_info.get(
                'menu', "OOPs,No menu available for this meal type.")
            bot.send_message(
                message.chat.id,
                f"🍽️ **{meal_type.capitalize()} Menu for {current_day.capitalize()}**:\n\n{menu_info['menu']}"
            )

            # Send the corresponding image
            image_url = menu_info.get('image', None)
            if image_url:
                bot.send_photo(message.chat.id, image_url)

            # Display options for further actions
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True)
            markup.add('Back', 'Main Menu')
            bot.send_message(message.chat.id,
                             "What would you like to do next?",
                             reply_markup=markup)

            # Wait for user to choose between Back or Main Menu
            bot.register_next_step_handler(message, navigate_menu, current_day)
        else:
            bot.send_message(message.chat.id,
                             "Wait please select your day first!!")
            greet_user(message)
    else:
        bot.send_message(message.chat.id,
                         "Invalid option. Please select a valid meal type.")
        select_meal_type(message)


# Navigation: Back or Main Menu
def navigate_menu(message, current_day):
    if message.text.lower() == "back":
        # Go back to meal selection for the selected day
        select_meal_type(message)
    elif message.text.lower() == "main menu":
        # Go back to the main day selection
        greet_user(message)
    else:
        bot.send_message(
            message.chat.id,
            "Invalid option. Please choose 'Back' or 'Main Menu'.")
        bot.register_next_step_handler(message, navigate_menu, current_day)


# Start polling
bot.polling()
