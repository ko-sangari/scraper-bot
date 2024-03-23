import os

from dotenv import load_dotenv

from utiles.city import AVAILABLE_CITY

load_dotenv()


class Settings:
    def __init__(self):
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        self.TELEGRAM_IDS = self._parse_telegram_ids(os.getenv("TELEGRAM_IDS"))
        self.SCHEDULER_TIMER = int(os.getenv("SCHEDULER_TIMER"))
        self.CITY_LIST = self._validate_city_list(os.getenv("CITY_LIST"))

    def _parse_telegram_ids(self, ids_str):
        """Convert a comma-separated string of IDs to a list of integers."""
        return [int(tid) for tid in ids_str.split(",") if tid.isdigit()]

    def _validate_city_list(self, cities_str):
        """Validate and return a list of City objects for the available city names."""
        requested_cities = cities_str.split(",")
        return [city for city in AVAILABLE_CITY if city.name in requested_cities]


settings = Settings()
