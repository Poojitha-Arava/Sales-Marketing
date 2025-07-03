# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'accounts/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'accounts/admin_dashboard.html')
    elif request.user.role == 'salesman':
        return render(request, 'accounts/sales_dashboard.html')
    elif request.user.role == 'marketing':
        return render(request, 'accounts/marketing_dashboard.html')
    else:
        return redirect('login')

@login_required
def analytics(request):
    return render(request, 'accounts/analytics.html')

@login_required
def lead_management(request):
    return render(request, 'accounts/lead_management.html')

def forgot_password_view(request):
    return render(request, 'accounts/forgot_password.html')