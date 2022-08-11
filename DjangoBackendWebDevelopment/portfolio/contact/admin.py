from django.contrib import admin
from .models import ContactList
from .models import ContactFrom
# Register your models here.

admin.site.register(ContactList)
admin.site.register(ContactFrom)
