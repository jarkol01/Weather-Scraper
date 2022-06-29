import requests
from bs4 import BeautifulSoup
from app.models.day import Day
import os

class Location():
    def __init__(self, name, average_temperature = 0, highest_propability_of_rain = 0, average_rain = 0, average_pressure = 0, average_humidity = 0, average_wind = 0, days = []):
        self.name = name
        self.average_temperature = average_temperature
        self.highest_propability_of_rain = highest_propability_of_rain
        self.average_rain = average_rain
        self.average_pressure = average_pressure
        self.average_humadity = average_humidity
        self.average_wind = average_wind
        self.days = days
    
    def extract_days(self):
        url = f'https://www.meteoprog.pl/pl/meteograms/{self.name}/'
        response = requests.get(url)
        page = BeautifulSoup(response.text, 'html.parser')

        if not os.path.exists("app/locations"):
            os.makedirs("app/locations")
        if not os.path.exists(f"app/locations/{self.name}"):
            os.makedirs(f"app/locations/{self.name}")

        for day in page.select('div.weather-details-hourly__item'):
            self.days.append(day.select_one('div.title').select_one('span').string)
            x = Day()
            x.extract_day(day)

            x.save_day(self.name)