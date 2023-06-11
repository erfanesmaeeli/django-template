# Generated by Django 4.1.7 on 2023-06-10 12:34

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='نام خانوادگی')),
                ('date_joined', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='تاریخ عضویت')),
                ('last_update', models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='آخرین ورود')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'آقا'), (2, 'خانم')], default=1, verbose_name='جنسیت')),
                ('phone', models.CharField(max_length=11, null=True, unique=True, verbose_name='تلفن همراه')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('valid_phone', models.BooleanField(default=False, verbose_name='تایید تلفن همره')),
                ('valid_email', models.BooleanField(default=False, verbose_name='تایید ایمیل')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': '   کاربران',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
