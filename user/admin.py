from django.contrib import admin
from . models import *

# Register your models here.
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
admin.site.register(CustomUser, CustomUserModelAdmin)

admin.site.register(Task)
