from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('some_text', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('employee/',include('employee.urls')),
]
