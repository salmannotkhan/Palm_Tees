from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from .forms import UserSignupForm, UserLoginForm
from .models import User

from django.template import Template, Context


def CustomLoginView(request):
    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                form.add_error('email', 'User doesn\'t exist')
            else:
                if user.is_active:
                    if user.verified_email:
                        password = form.cleaned_data.get('password')
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            login(request, user)
                            return redirect('index')
                        else:
                            form.add_error('password', 'Incorrect login details')
                    else:
                        form.add_error('email', 'Please verify your account before login')
                else:
                    form.add_error('email', 'You\'re account has been blocked because of malicious activity')
            finally:
                pass
        else:
            for field in form.errors:
                print(field)
    context = {
        'form': form,
    }
    return render(request, 'account/login.html', context)

def ProfileView(request):
    context = {

    }
    return render(request, 'account/profile.html', context)


def SignupView(request):
    form = UserSignupForm(request.POST or None)
    
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.verified_email = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your PalmTees Account'

            message = render_to_string('emails/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject, message, recipient_list=[user.email], from_email=None, html_message=message)
            
            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'account/signup.html', context)

def ActivateAccountView(request,uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.verified_email = True
        user.save()
        login(request, user)
        messages.success(request, ('Your account have been confirmed.'))
        return redirect('index')
    else:
        messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('index')