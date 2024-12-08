from datetime import datetime

import requests

from weather import Weather


class API:
    def __init__(
            self,
            api_key,
            base_url='http://dataservice.accuweather.com/'
    ):
        self.base_url = base_url
        self.api_key = api_key

    def location_key(self, city_name):
        req = requests.get(url=f'{self.base_url}locations/v1/cities/search',
                           params={
                               'apikey': self.api_key,
                               'q': city_name,
                               'language': 'en-us',
                               'details': 'true'
                           })
        res = req.json()
        return res[0]['Key']

    def weather(self, city_name):
        location_key = self.location_key(city_name)
        req = requests.get(url=f'{self.base_url}forecasts/v1/daily/5day/{location_key}',
                           params={
                               'apikey': self.api_key,
                               'language': 'en-us',
                               'details': 'true',
                               'metric': 'true'
                           })
        res = req.json()
        lst = list()
        for day in res['DailyForecasts']:
            for day_part in ['Day', 'Night']:
                lst.append(
                    Weather(day=datetime.fromisoformat(day['Date']).date(),
                            day_part=day_part,
                            location=city_name,
                            rain_probability=day[day_part]['RainProbability'],
                            humidity=day[day_part]['RelativeHumidity']['Average'],
                            wind_speed=day[day_part]['Wind']['Speed']['Value'],
                            temperature=(day['Temperature']['Minimum']['Value'] +
                                         day['Temperature']['Maximum']['Value']) / 2)
                )
        return lst