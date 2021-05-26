from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/user.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        userpassword = request.POST['password']
        user = authenticate(request, username=username, password=userpassword)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                "message": 'invalid credentials'
            })

    return render(request, 'users/login.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
