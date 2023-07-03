from django.shortcuts import render

from django.shortcuts import render

from fishbook.weather.weather_api_service import get_weather_data_for_searched_city, get_forecast_data_for_searched_city


def weather_view(request):
    city = request.GET.get('city')

    if city:
        current_weather_data = get_weather_data_for_searched_city(city)
        forecast_data = get_forecast_data_for_searched_city(city)

        if current_weather_data and forecast_data:
            return render(request, 'weather/show_weather_data.html', {'current_weather_data': current_weather_data, 'forecast_data': forecast_data})
        else:
            error_message = 'Failed to fetch weather data for the requested city.'
            return render(request, 'weather/show_weather_data.html', {'error_message': error_message})
    else:
        return render(request, 'weather/show_weather_data.html')
