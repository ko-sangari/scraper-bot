# Welcome to Scraper Bot
I wrote this bot for myself to find accommodation on https://holland2stay.com.\
I'll be happy if it can help improve your experience in searching for your desired accommodation.

## ✫ Features
Scraping the website every 2 minutes, check for any available accommodations and sends them to your Telegram account.

## ✫ Configuration

### ○ Install the requirements:
```
pip install -r requirements.txt
```

### ○ Telegram Token:
> Create a new bot on Telegram and obtain the bot token.

Now, Create a ```.env``` file in root directory and add a line like this:
```
TELEGRAM_TOKEN=your-telegram-token
```

### ○ User Telegram ID:
The bot should have the Telegram ID for each user in order to send notifications to them.\

Run the Telegram bot:
```
python telegram.py
```
and send the start command in chat: ```/start```\
Now you can see your Telegram ID, and update that ID in ```scraper_holland2stay.py```\
You don't need it to be running anymore.
### ○ Run the Scraper bot:
Lastly, keep this command running for as long as you need.
```
python run.py
```
## ✫ Contributions
Contributions are welcome!\
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## ✫ Disclaimer
Please use this bot responsibly and respect the terms of service of the website you are scraping.\
Be mindful of the website's policies and considerate of the server load when using the bot extensively.