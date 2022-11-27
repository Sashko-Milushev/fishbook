from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from fishbook.accounts.views import SignUpView, SignOutView, SignInView, UserEditView, UserDeleteView, UserDetailsView, \
    add_profile, details_profile, edit_profile

urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('user/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
    path('profile/', include([
        path('create/', add_profile, name='create profile'),
        path('<int:pk>/', include([
            path('details/', details_profile, name='details profile'),
            path('edit/', edit_profile, name='edit profile'),
        ])),
    ])),

]

from .signals import *
