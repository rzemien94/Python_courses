from django.contrib import admin
from .models import About
from .models import Slider
from .models import Client

# Register your models here.

admin.site.register(About)
admin.site.register(Slider)
admin.site.register(Client)
