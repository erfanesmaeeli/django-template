from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VerificationCode, User
from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .validators import phone_validation
from django.urls import reverse_lazy


# ------------------------------ User Login ------------------------------
def login_view(request):
    form = LoginForm(request.POST or None)
    error = None
    template_name = "accounts/login.html"
    
    if request.method == 'GET':
        if 'next' in request.GET:
            request.session['next'] = request.GET['next']

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.session:
                    return redirect(request.session['next'])
                return redirect('/')
            else:
                error = 'نام کاربری یا کلمه عبور صحیح نمی ‌باشد!'
        else:
            error = 'خطا در اعتبارسنجی فرم'
    return render(request, template_name, {"form": form, "error": error})


# ------------------------------ User SignUp ------------------------------
def signup_view(request):
    template_name = "accounts/signup.html"
    context = {}
    form = SignUpForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            if not phone_validation(phone):
                form.add_error('phone', 'تلفن همراه معتبر نمی‌باشد.')
            else:
                form.save()
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=phone, password=raw_password)
                login(request, user)
                
                # if need phone verisication
                return redirect('accounts:send-phone-verification')
        
    context["form"] = form
    return render(request, template_name, context)



class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.request.user
        return context


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'phone', 'gender', 'email', 'date_of_birth']
    template_name = 'profiles/profile_update.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        user = self.request.user
        
        if not user.is_superuser:
            # only get the user's own profile
            queryset = queryset.filter(Q(id=user.id))
            obj = get_object_or_404(queryset)
        else:
            obj = get_object_or_404(queryset)
        return obj
    

# ------------------------------ User verifications ------------------------------
# ------------------------------ Phone verification ------------------------------
@login_required
def send_phone_verification(request):
    user = request.user
    try:
        new_vertify_code = VerificationCode.objects.create(user=user, subject="phone")
    except Exception as e:
        print(e)
        messages.error(request, "خطا در ایجاد کد تایید!")
        return redirect('accounts:phone-verification-check')
    else:
        data = {
            "receptor": user.phone,
            "token": new_vertify_code.code,
            "template": 'phone-verification'
        }            
    
        # if send_sms(data, 'phone_verify', user):
        #     return redirect('accounts:phone-verification-check')
        # else:
        #     messages.error(request, "خطا در ارسال پیامک کد تایید!")
        #     return redirect('accounts:phone-verification-check')
        

@login_required()
def phone_verification(request):
    template_name = 'accounts/phone_verification.html'
    context = {}

    if request.method == 'POST':
        user = request.user
        if not user.phone:
            messages.error(request, "تلفن همراه خود را در مشخصات فردی ثبت نمایید!")
            return redirect('accounts:phone-verification')
        
        send_vcode = request.POST.get('send_vcode', None)
        if send_vcode == '1':
            try:
                new_vertify_code = VerificationCode.objects.create(user=user, subject="phone")
            except Exception as e:
                messages.error(request, "خطا در ایجاد کد تایید!")
                return redirect('accounts:phone-verification')
            
            data = {
                "receptor": user.phone,
                "token": new_vertify_code.code,
                "template": 'phone-verification'
            }            
            
            # if send_sms(data, 'phone_verification', user):
            #     return redirect('accounts:phone-verification-check')
            # else:
            #     messages.error(request, "خطا در ارسال پیامک کد تایید!")
            #     return redirect('accounts:phone-verification')
                
    return render(request, template_name, context)



@login_required()
def phone_verification_check(request):
    template_name = 'accounts/phone_verification_check.html'
    context = {}

    if request.method == 'POST':
        v_code = request.POST.get('v_code', None)
        if v_code:
            the_user = request.user
            verify = VerificationCode.objects.filter(user=the_user, subject='phone', status=1)
            if verify.exists():
                verify = verify.last()
                if verify.code == v_code:
                    the_user.valid_phone = True
                    the_user.save()
                    verify.attempts += 1
                    verify.status = 2
                    verify.save()
                    return redirect("accounts:phone-verification-done")
                else:
                    verify.attempts += 1
                    if verify.attempts >= 5:
                        verify.status = 0
                    verify.save()
                    messages.error(request, "کد تایید نامعتبر است!")
                    return render(request, template_name, context)
            else:
                messages.error(request, "کد تایید منقضی شده است!")
                return redirect('accounts:phone-verification-check')
    return render(request, template_name, context)


class PhoneVerificationDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/phone_verification_done.html'