from django.urls import path

from fishbook.photos.views import add_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
)
