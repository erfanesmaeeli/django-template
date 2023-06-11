from django.urls import path
from .views import (
    login_view,
    signup_view,
    ProfileView,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
