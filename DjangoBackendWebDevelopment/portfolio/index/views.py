from django.shortcuts import render
from .models import About
from .models import Slider
from .models import Client

# Create your views here.
def home(request):
    about_data=About.objects.all()[0]
    slider_data=Slider.objects.all()
    client_data=Client.objects.all()
    context={
        'about': about_data,
        'slider': slider_data,
        'client': client_data
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')
