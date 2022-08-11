from django.shortcuts import render
from .models import ContactList
from .models import ContactFrom

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_form_data = ContactFrom(name=name,email=email,subject=subject,message=message)
        contact_form_data.save()

    contact_list_data=ContactList.objects.all()[0]
    context={
        'contact_list': contact_list_data,
    }
    return render(request,'contact.html',context)
