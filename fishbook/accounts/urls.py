from django.urls import path, include

from fishbook.accounts.views import SignUpView, SignOutView, SignInView, UserEditView, UserDeleteView, UserDetailsView, add_profile

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('user/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
    path('profile/', add_profile, name='create profile'),

)