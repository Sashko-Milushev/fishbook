import requests
from decouple import config

api_key = config('WEATHER_API_KEY')


def get_weather_data_for_searched_city(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_data = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'wind_speed': data['wind']['speed'],
            'humidity': data['main']['humidity'],
            'precipitation': data.get('rain', {}).get('1h', 0),
            'pressure': data['main']['pressure']
        }

        return weather_data
    else:
        return None

