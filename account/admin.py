from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UcUser

admin.site.register(UcUser, UserAdmin)

# Register your models here.


