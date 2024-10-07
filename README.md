
# Telegram Food Menu Bot

This is a Telegram bot built using Python's `telebot` library. The bot provides daily food menus for various meals including breakfast, lunch, snacks, and dinner, along with images for each dish.

## Features

- Get the menu for a specific day and meal (breakfast, lunch, snacks, dinner).
- Receive an image along with the meal description.
- Easy to extend for additional days or meal types.

### Requirements

- Python 3.x
- The `pyTelegramBotAPI` package (also known as `telebot`)

Install dependencies using pip:

```bash
pip install pyTelegramBotAPI
```

### Telegram Bot Token

To use this bot, you will need a Telegram Bot API token. You can obtain this by talking to [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

Once you have your token, replace the placeholder in the `API_TOKEN` variable in the script:

```python
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
```

### Running the Bot

To run the bot, simply execute the Python script:

```bash
python telegram_bot.py
```

Ensure that your bot is set up and configured in Telegram, and you have set the webhook or are using long polling.

## How it Works

1. **Daily Menu Storage**: The bot uses a dictionary to store menus for each day of the week (e.g., Monday to Sunday). Each day contains details for:
    - Breakfast
    - Lunch
    - Snacks
    - Dinner

2. **Menu Display**: Users can request a menu for a specific day and meal type. The bot responds with a description of the meal and a relevant image.

3. **Telebot Commands**: The bot uses the `telebot` package to handle messages and interact with the user.

## Example Menu Structure

```python
menus = {
    "monday": {
        "breakfast": {
            "menu": "Pav Bhaji, Tea",
            "image": "https://www.example.com/pavbhaji.jpg"
        },
        "lunch": {
            "menu": "Mix Veg, Dal Fry, Green Peas Pulao, Raita, Chapati and Fruits",
            "image": "https://www.example.com/lunch.jpg"
        }
    }
}
```

## Extending the Bot

To add more menus or modify existing ones, simply update the `menus` dictionary with new days or meals.

## License

This project is licensed under the MIT License.
