from django.shortcuts import render
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from django.views import generic as views


from fishbook.accounts.forms import SignUpForm


class SignInView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return self.get_redirect_url() or self.get_default_redirect_url()


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login user')


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('home')