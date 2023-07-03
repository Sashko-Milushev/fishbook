from django.urls import path

from fishbook.weather.views import weather_view

urlpatterns = (
    path('', weather_view, name='weather'),

)