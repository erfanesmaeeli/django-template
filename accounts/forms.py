# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - sharifdata sdata.ir
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VerificationCode
from django.db.models import Q

# ------------------------------ User SignUp ------------------------------
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'gender', 'password1', 'password2')


# ------------------------------ User Login ------------------------------
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "نام کاربری",
                "class": "form-control",
                "title": ""
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "کلمه عبور",
                "class": "form-control",
                "title": ""
            }
        ))