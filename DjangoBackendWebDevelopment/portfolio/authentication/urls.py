from django.urls import path
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('registration', views.registration,name='registration'),
    path('forget-password', views.forget_password,name='forget_password'),
]
