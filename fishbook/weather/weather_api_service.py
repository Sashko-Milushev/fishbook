import requests
from decouple import config

api_key = config('WEATHER_API_KEY')


def get_weather_data_for_searched_city(city_name):
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    current_weather_response = requests.get(current_weather_url)

    if current_weather_response.status_code == 200:
        current_weather_data = current_weather_response.json()

        current_weather_data = {
            'city': city_name,
            'description': current_weather_data['weather'][0]['description'],
            'icon': current_weather_data['weather'][0]['icon'],
            'temperature': current_weather_data['main']['temp'],
            'feels_like': current_weather_data['main']['feels_like'],
            'wind_speed': current_weather_data['wind']['speed'],
            'humidity': current_weather_data['main']['humidity'],
            'precipitation': current_weather_data.get('rain', {}).get('1h', 0),
            'pressure': current_weather_data['main']['pressure'],
        }

        return current_weather_data
    else:
        return None


def get_forecast_data_for_searched_city(city_name):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        forecast_data = []
        for forecast in data['list']:
            forecast_entry = {
                'city': city_name,
                'datetime': forecast['dt_txt'],
                'description': forecast['weather'][0]['description'],
                'icon': forecast['weather'][0]['icon'],
                'temperature': forecast['main']['temp'],
                'feels_like': forecast['main']['feels_like'],
                'wind_speed': forecast['wind']['speed'],
                'humidity': forecast['main']['humidity'],
                'precipitation': forecast.get('rain', {}).get('3h', 0),
                'pressure': forecast['main']['pressure'],
            }
            forecast_data.append(forecast_entry)

        return forecast_data
    else:
        return None
