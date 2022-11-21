from django.urls import path

from fishbook.common.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)