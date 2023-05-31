import requests
from bs4 import BeautifulSoup
from datetime import datetime

from telegram import direct_message
from utiles import City


user_one = 123456789    # User's Telegram ID.

# List of cities that you want to check. Find the ID on the site.
CITY_LIST = [
    City(id=24,  name='Amsterdam', clients=[user_one]),
]

# List of URLs that you don't want to be disturbed by.
EXCEPTIONS = [
    'https://holland2stay.com/blah-blah.html',
]


def scraper(_city: City):
    url = f"https://holland2stay.com/residences.html?available_to_book=179&city={_city.id}"

    page = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            }
        )

    bsoup = BeautifulSoup(page.content, "html.parser")
    card_list = bsoup.find_all('div', class_='regi-item')

    for card in card_list:
        tags = card.select("div.regi-center div.item-head h4 span")

        data = {
            "link": card.select("div.regi-img a")[0]['href'],
            "location": card.select("div.regi-center ul.regi-info li:nth-child(2) span")[0].get_text(),
            "title": card.select("div.regi-center div.item-head h4.regularbold")[0].find(text=True, recursive=False),
            "building": card.select("div.regi-center ul.regi-info li:nth-child(3) span")[0].get_text(),
            "tags": [pt.get_text() for pt in tags],
            "available_from": card.select("div.regi-center ul.regi-info li strong")[0].get_text(),
            "price": card.select("div.regi-right div.regi-price div.price")[0].get_text().replace('\u20ac', ''),
        }

        if data['link'] not in EXCEPTIONS:
            for telegram_id in _city.clients:
                direct_message(telegram_id, data)

    print(f"> {datetime.now().replace(microsecond=0)} | {len(card_list)} item found for {_city.name}")


for city in CITY_LIST:
    scraper(city)
