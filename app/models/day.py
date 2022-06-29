import json

class Day():
    def __init__(self, date = '', temperature = [], propability_of_rain = [], rain = [], pressure = [], humidity = [], wind = []):
        self.date = date
        self.temperature = temperature
        self.propability_of_rain = propability_of_rain
        self.rain = rain
        self.pressure = pressure
        self.humidity = humidity
        self.wind = wind
    
    def extract_day(self, day):
        self.date = day.select_one('div.title').select_one('span').string
        self.temperature = [int(x.select_one('span').string[:-1]) for x in day.select('div.temperature__column')]
        self.propability_of_rain = [int(x.select_one('span').string[:-1]) for x in day.select('div.rain-probability__column')]
        self.rain = [float(x.select_one('span').string.replace(',', '.')) for x in day.select('div.rain-level__column')]
        self.pressure = [int(x.select_one('span').string) for x in day.select('div.pressure-level__column')]
        self.humidity = [int(x.string[:-1]) for x in day.select('tr > td > span')]
        self.wind = [int(x.select_one('span').string) for x in day.select('div.wind-speed__column')]
    
    def save_day(self, name):
        day_dict = {
            'temperature': self.temperature,
            'propability_of_rain': self.propability_of_rain,
            'rain': self.rain,
            'pressure': self.pressure,
            'humidity': self.humidity,
            'wind': self.wind
        }
        with open(f'app/locations/{name}/{self.date}.json', "w", encoding="UTF-8") as file:
            json.dump(day_dict, file, indent=4, ensure_ascii=False)