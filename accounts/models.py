from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser
from .validators import phone_number_validator, limit_file_size
from main.models import General
from django.db.models import Q
from jalali_date import datetime2jalali, date2jalali
from datetime import datetime


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'آقا'),
        ('female', 'خانم'),
        ('other', 'سایر'),
    ]
    
    first_name = models.CharField(verbose_name="نام", max_length=30, null=True, blank=False)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=50, null=True, blank=False)
    date_joined = models.DateTimeField(verbose_name="تاریخ عضویت", null=True, blank=True, default=datetime.now)
    last_update = models.DateTimeField(verbose_name="آخرین بروزرسانی", auto_now=True, null=True)
    last_login = models.DateTimeField(verbose_name="آخرین ورود", null=True, blank=True)
    gender = models.CharField(verbose_name="جنسیت", max_length=10, choices=GENDER_CHOICES, default='m')
    phone = models.CharField(verbose_name="تلفن همراه", null=True, blank=True, \
        max_length=11)
    email = models.EmailField(verbose_name="ایمیل", null=True, blank=True)
    valid_phone = models.BooleanField(default=False, verbose_name="تایید تلفن همره")    
    valid_email = models.BooleanField(default=False, verbose_name="تایید ایمیل")

    class Meta:
        verbose_name_plural = '   کاربران'
        verbose_name = 'کاربر'

    def get_date_joined(self):
        if self.date_joined:
            return datetime2jalali(self.date_joined).strftime("%H:%M - %Y/%m/%d")
        return 'بدون تاریخ'
    get_date_joined.short_description = 'تاریخ و زمان عضویت'

    def get_date_joined__date(self):
        if self.date_joined:
            return datetime2jalali(self.date_joined).strftime("%Y/%m/%d")
        return 'بدون تاریخ'  
    get_date_joined__date.short_description = 'تاریخ عضویت'

    def get_last_update(self):
        if self.last_update:
            return datetime2jalali(self.last_update).strftime("%H:%M - %Y/%m/%d")
        return 'بدون تاریخ'
    get_last_update.short_description = 'آخرین بروزرسانی'

    def get_last_login(self):
        if self.last_login:
            return datetime2jalali(self.last_login).strftime("%H:%M - %Y/%m/%d")
        return "تاکنون وارد سایت نشده است."
    get_last_login.short_description = 'آخرین ورود'

    def get_gender(self):
        if self.gender == 'male':
            return 'آقای'
        elif self.gender == 'female':
            return 'خانم'
        elif self.gender == 'other':
            return 'سایر'
        else:
            return 'نامعتبر'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__previous_phone = self.phone
            self.__previous_email = self.email

    def save(self, *args, **kwargs):   
        super(User, self).save()