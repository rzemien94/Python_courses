from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/registration.html')

def forget_password(request):
    return render(request,'authentication/forget.html')
