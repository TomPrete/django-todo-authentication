from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_user(request):
    if request.method == "POST":
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login_user'))
        else:
            return redirect(reverse('accounts:signup_user'))
    if request.method == 'GET':
        form = SignUpUserForm()
        return render(request, 'accounts/signup.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            valid_user = authenticate(username=username, password=password)
            if valid_user:
                login(request, valid_user)
                return redirect('/')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Your username or password is incorrect.'})
    if request.method == 'GET':
        form = LoginUserForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('accounts:login_user'))
