from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from datetime import datetime, timedelta


class DemoView(generic.TemplateView):
    template_name = 'demo/index.html'