from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import User

class CustomModelBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if '@' in username:
            kwargs = {'email': username}
        elif username.isdigit():
            kwargs = {'phone': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None