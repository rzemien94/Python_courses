from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('some_text', views.aboutus,name='about'),
]
