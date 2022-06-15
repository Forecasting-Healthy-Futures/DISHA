# Weather Forcast for temperature and rainfall for a lat lon

import numpy as np
import requests


class WeatherForecast:

    def __init__(self, latitude, longitude, day):
        self.latitude = latitude
        self.longitude = longitude
        self.url = 'https://api.openweathermap.org/data/2.5/onecall?'
        self.key = '7512fdb494159d06979fd54b386cde04'
        self.exclude = " "
        self.day = day

    def get_geolocation(self):
        from geopy.geocoders import Nominatim

        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")

        # Latitude & Longitude input
        Latitude = f"{self.latitude}"
        Longitude = f"{self.longitude}"

        location = geolocator.reverse(Latitude + "," + Longitude)

        return location

    def get_weather_forecast(self):
        # get the weather forecast
        url = self.url + 'lat=' + str(self.latitude) + '&lon=' + str(
            self.longitude) + '&exclude=' + self.exclude + '&appid=' + self.key
        response = requests.get(url)
        data = response.json()

        return data

    def forecast_weather(self):

        x = self.get_weather_forecast()

        print(f"The weather forecast for {self.get_geolocation()} is as follows:")
        print(f"The Humidity forecast for for Day {self.day}: {x['daily'][self.day]['humidity']}")
        print(
            f"The Minimum Temperature forecast for for Day {self.day}: {np.round(x['daily'][self.day]['temp']['min'] - 273.15, 2)} ")
        print(
            f"The Maximum Temperature forecast for for Day {self.day}: {np.round(x['daily'][self.day]['temp']['max'] - 273.15, 2)}")
        print(
            f"The Average Temperature forecast for for Day {self.day}: {np.round(x['daily'][self.day]['temp']['day'] - 273.15, 2)}")
        if 'rain' not in x['daily'][self.day]:
            print(f"The Rain forecast for for Day {self.day}: 0 mm {x['daily'][self.day]['weather'][0]['description']}")
        else:
            print(
                f"The Rain forecast for for Day {self.day}: {x['daily'][self.day]['rain']}mm {x['daily'][self.day]['weather'][0]['description']}")
#
#
# if __name__ == "__main__":
#     # get the weather forecast
#     x = weather_forecast(latitude=25.2702, longitude=91.7323, day=2)
#     # x = weather_forecast(latitude=19.2183, longitude=72.9781, day=2)
#     x.forecast_weather()