from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.user.is_authenticated:
        return redirect("reservationapp:list")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservationapp:list')
        else:
            messages.info(request, 'Votre email ou mot de passe est incorrect')
    return render(request, 'accounts/login.html')



@login_required(login_url='accounts:login')
def disconnect(request):
    logout(request)
    return redirect('accounts:login')

