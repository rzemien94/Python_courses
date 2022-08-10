from django.shortcuts import render
from .models import ContactList

# Create your views here.
def contactus(request):
    contact_list_data=ContactList.objects.all()[0]
    context={
        'contact_list': contact_list_data,
    }
    return render(request,'contact.html',context)
