from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import StudentInfo


# Create your views here.
def Home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('home')
    return render(request, 'manager/home.html')

def Dashboard(request):
    context = {
        'infos': StudentInfo.objects.all()
    }
    return render(request, 'manager/dashboard.html', context)