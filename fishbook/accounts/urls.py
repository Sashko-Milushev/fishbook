from django.urls import path

from fishbook.accounts.views import SignInView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
)