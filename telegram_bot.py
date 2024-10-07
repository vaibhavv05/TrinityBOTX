import telebot
from telebot import types

API_TOKEN = '7857970440:AAG7D4Uawz14-HFnBQzYb7uOYAaZPl0NNuA'

bot = telebot.TeleBot(API_TOKEN)

# Dictionary to store the menu for each day and meal type
menus = {
    "monday": {
        "breakfast": {
            "menu":
            "Pav Bhaji, Tea",
            "image":
            "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/pav-bhaji-1.jpg"
        },
        "lunch": {
            "menu":
            "Mix Veg, Dal Fry, Green Peas Pulao, Raita, Chapati and Fruits",
            "image":
            "https://preview.redd.it/veg-thali-rajma-masala-masoor-dal-mattar-pulao-palak-raita-v0-7x702xtcy8ja1.jpg?width=1080&crop=smart&auto=webp&s=632bcc0b6ab1c6047d9d061f863368a658ccfb2a"
        },
        "snacks": {
            "menu":
            "Masala Pav, Tea",
            "image":
            "https://madhurasrecipe.com/wp-content/uploads/2020/10/Masala-Pav-Marathi-Recipe.jpg"
        },
        "dinner": {
            "menu":
            "Matar Paneer/ Palak Paneer (As per season), Black Dal, Plain Rice, Shahi Tukda, Chapati",
            "image":
            "https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/matar-paneer-0.jpg"
        }
    },
    "tuesday": {
        "breakfast": {
            "menu":
            "Poha, Black Chana/ Dalia (Alternative Week), Coconut Chutney, Coffee",
            "image":
            "https://media.vogue.in/wp-content/uploads/2020/10/poha-recipe-1920x1080.jpg"
        },
        "lunch": {
            "menu":
            "Rajma Masala, Aloo Bhindi Dry, Plain Rice, Curd, Salad, Chapati and Fruits",
            "image":
            "https://www.secondrecipe.com/wp-content/uploads/2017/08/rajma-chawal-1-720x551.jpg"
        },
        "snacks": {
            "menu":
            "Samosa, Chutney, Tea",
            "image":
            "https://www.awesomecuisine.com/wp-content/uploads/2014/11/vegetable-samosa.jpg"
        },
        "dinner": {
            "menu":
            "Chhole Masala, Dal Fry, Masala Rice, Methi Roti, Sheera",
            "image":
            "https://pipingpotcurry.com/wp-content/uploads/2017/05/Instant-Pot-Chana-Masala.-Chole.-Chickpeas.jpg"
        }
    },
    "wednesday": {
        "breakfast": {
            "menu":
            "Idli, Sambhar/ Coconut Chutney (Alternative Week), Tea",
            "image":
            "https://vaya.in/recipes/wp-content/uploads/2018/02/Idli-and-Sambar-1.jpg"
        },
        "lunch": {
            "menu":
            "Dal Makhni, Chana Cabbage Dry, Zeera Rice, Curd, Chapati and Fruits",
            "image":
            "https://www.cookwithmanali.com/wp-content/uploads/2019/04/Restaurant-Style-Dal-Makhani.jpg"
        },
        "snacks": {
            "menu":
            "Vada Pav, Tea",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYPjqgA4mp3J-T5DBx6oucBYC5v_WligkX8w&s"
        },
        "dinner": {
            "menu":
            "Paneer Kofta/ Chicken Curry, Dal Fry, Rice, Chapati, Fruit Custard",
            "image":
            "https://cdn3.foodviva.com/static-content/food-images/curry-recipes/paneer-kofta-recipe/paneer-kofta-recipe.jpg"
        }
    },
    "thursday": {
        "breakfast": {
            "menu":
            "Puri Bhaji, Tea",
            "image":
            "https://maayeka.com/wp-content/uploads/2014/07/poori-bhaji-aloo-tamatar-sabzi.jpg"
        },
        "lunch": {
            "menu":
            "Veg Biryani, Curry, Papad, Raita and Fruits",
            "image":
            "https://theartisticcook.com/wp-content/uploads/2024/01/Vegetablebiryani1.jpg"
        },
        "snacks": {
            "menu":
            "Poha, Chutney, Coffee",
            "image":
            "https://media.vogue.in/wp-content/uploads/2020/10/poha-recipe-1920x1080.jpg"
        },
        "dinner": {
            "menu":
            "Aloo Gobhi/ Veg Tawa (Alternative Week), Chana Dal Palak, Zeera Rice, Ajwain Chapati,Gulab Jamun",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrEhyeJ7g4kKXTqwY5oF14ryu3pmLNiiBg5A&s"
        }
    },
    "friday": {
        "breakfast": {
            "menu":
            "Bread Butter Jam, Veg Cutlet/ Boiled Eggs (2 Pcs), Tea",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKAVql9OeIiznXgM5DVVbrt_ffBQkwObq5Tw&s"
        },
        "lunch": {
            "menu":
            "Aloo Matar, Dahi Kadhi and Onion Pakoda (2 Pcs), Plain Rice, Salad, Roti and Fruits",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7bo36uK3-WAigkTIpM9qTLk0J6e4fKSanKA&s"
        },
        "snacks": {
            "menu":
            "Bread Pakoda, Chutney, Tea",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtO9oQyHjXVgCWUkZY-VdIoMjFht5Ep-T6GQ&s"
        },
        "dinner": {
            "menu":
            "Paneer Kadai/ Egg Curry, Plain Rice, Dal Fry, Chapati, Shevai Kheer",
            "image":
            "https://www.funfoodfrolic.com/wp-content/uploads/2020/12/Kadhai-Paneer-Thumbnail.jpg"
        }
    },
    "saturday": {
        "breakfast": {
            "menu":
            "Aloo Paratha, Curd, Tea",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL0Zq6X0Ih5ODzljjrNF4CqOmXIDazdidGSA&s"
        },
        "lunch": {
            "menu":
            "Methi Roti/ Chhole Bhature (Alternative Week), Chhole Masala, Rice, Dal Fry, Boondi Raita, Salad and Fruits",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSHuqEQvNy--dkfLm4j4WW74dgvb2tb4HilQ&s"
        },
        "snacks": {
            "menu":
            "Bhel (Onion+Chilies incl.), Coffee",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj3fb1raHsOqjESFwLP_P5wVEGg5gi1Cb6dg&s"
        },
        "dinner": {
            "menu":
            "Soyabean Sabzi, Masoor Dal Fry, Masala Rice, Chapati, Rice Kheer/Chinese Food(Chow Mein, Fried Rice, Soup)(Alternative Week)",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgXRbxDjMPkdfsE1It1wcf7fEqRw5x_yUHmA&s"
        }
    },
    "sunday": {
        "breakfast": {
            "menu":
            "Onion-Tomato Uttapam/ Veg Upma, Sambhar, Tea",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGf8TNraePqjNMbzCCyxlqaQJmkMquUfbicA&s"
        },
        "lunch": {
            "menu":
            "Black Chana Masala, Dal Fry, Rice, Raita, Chapati and Fruits",
            "image":
            "https://www.indianveggiedelight.com/wp-content/uploads/2023/01/kala-chana-curry-recipe-featured.jpg"
        },
        "snacks": {
            "menu":
            "Cream Bun, Tea",
            "image":
            "https://www.bigbasket.com/media/uploads/p/l/60000891_2-fresho-cream-bun-vanilla-flavour-freshly-baked.jpg"
        },
        "dinner": {
            "menu":
            "Aloo Palak/ Aloo Matar(As per season), Pancharatna Dal, Green Peas Pulav, Puri/ Methi Roti, Sabudana Kheer",
            "image":
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgUeMaMBhP9QCn7mo8gtCSlLyKkuCW3vQpWQ&s"
        }
    }
}

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

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       resize_keyboard=True)
    days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    for day in days:
        markup.add(day)

    bot.send_message(message.chat.id,
                     "Hello! Please select a day of the week:",
                     reply_markup=markup)


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
                f"The menu for {meal_type.capitalize()} on {current_day.capitalize()} is: {menu_text}"
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
