from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text={
        'name':'Mateusz Rzemieniewski',
        'age':28,
        'phone':123123123,
        'friend_name':['Mateusz','some_text','example1']
    }
    return render(request,'index.html',text)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
