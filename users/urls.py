from django.urls import path
from users.views import UserLoginView, UserRegistrationView, UserProfileView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
