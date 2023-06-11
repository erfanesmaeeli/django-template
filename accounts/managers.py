from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validators import phone_validation

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Users must have a phone number')
        
        if not phone_validation(phone):
            raise ValueError('Phone number is not valid!')

        user = self.model(phone=phone, username=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('valid_phone', True)
        extra_fields.setdefault('valid_email', True)
        extra_fields.setdefault('first_name', 'Super')
        extra_fields.setdefault('last_name', 'Admin')
        phone = phone
        
        return self.create_user(phone, password, **extra_fields)