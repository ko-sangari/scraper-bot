# 🤖 Welcome to Scraper Bot
I wrote this bot for myself to find accommodation on **[holland2stay](https://holland2stay.com)** website. \
I'll be happy if it can help improve your experience in searching for your desired accommodation.

## ⭕ Features
Scraping the website every 2 minutes, check for any available accommodations and sends them to your Telegram account.

## ⭕ Before you begin
Before you begin, please follow these steps:

### 💢 Add `.env` file :

1. Rename the `.env.template` file to `.env`.
2. Update the variables in the `.env` file according to your local environment.


### 💢 Setting Up a Telegram Bot :

To use this application, you'll need to create a Telegram bot and obtain its token. Here's how you can do it:

1. **Start a Chat with BotFather**: BotFather is Telegram's official bot for creating and managing other bots. Open your Telegram app and search for `@BotFather`. Start a chat with it.

2. **Create a New Bot**: In the chat with BotFather, send the command `/newbot`. BotFather will ask you for a name and username for your new bot. Follow the prompts and provide the necessary information.

3. **Save Your Bot Token**: After your bot is created, BotFather will provide a token for your bot. This is a unique string that allows you to control your bot via the Telegram API. Copy and save this token securely.

4. **Set the Token in Your Environment**: Place the bot token in the `.env` file. This is usually done by adding a line like `TELEGRAM_TOKEN=your_token_here` in the `.env` file.

By following these steps, you'll have a new Telegram bot and its associated token, ready to be used with this application.


### 💢 Find the Telegram User ID :
Now, to add Telegram clients, it's essential to acquire their respective Telegram IDs. To do this, you need to follow these steps:

1. **Search for the UserInfo Bot**:
   Open Telegram and search for `@userinfobot`. This bot can provide your user information, including your user ID.

2. **Start the Bot**:
   Click on the bot in the search results to open a chat, then click the "Start" button at the bottom of the chat window.

3. **Get Your ID**:
   The bot will automatically send you a message that includes your user ID and other details. Your Telegram user ID can be found in this message. To use it, add your ID to the `.env` file by inserting a line such as `TELEGRAM_IDS=123456789`.

## ⭕ How To Run the Project

### 💢 Install the requirements :
To run the project, you first need to have `poetry` installed:
```commandline
pip install poetry
poetry install
```

### 💢 Run the Scraper bot :
Lastly, keep this command running for as long as you need.
```
poetry run python core/run.py
```
## ⭕ Contributions
Contributions are welcome!\
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## ⭕ Disclaimer
Please use this bot responsibly and respect the terms of service of the website you are scraping.\
Be mindful of the website's policies and considerate of the server load when using the bot extensively.
