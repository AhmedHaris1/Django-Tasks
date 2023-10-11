from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from allauth.account.forms import LoginForm, SignupForm
import logging
# from django.conf import settings

logger = logging.getLogger(__name__)

def home(request):
    # email = settings.EMAIL_HOST_USER
    return render(request, 'home.html',)
 
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return login(request, user)
        else:
            context = {'form': form}
            return render(request, 'account/login.html', context)
    else:
        form = LoginForm(request)

    context = {'form': form}
    return render(request, 'account/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            logger.error('Form Errors: &s', form.errors)
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)

def password_reeset(request):
    return render(request, 'account/password_reset_form.html')