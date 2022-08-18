from django.urls import path
from . import views

urlpatterns = [
    path('', views.authlogin,name='login'),
    path('registration', views.authregistration,name='registration'),
    path('forget-password', views.forget_password,name='forget_password'),
]
