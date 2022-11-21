from django.shortcuts import render
from django.contrib.auth import views as auth_view


class SignInView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'
