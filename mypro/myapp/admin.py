from django.contrib import admin
from .models import Marolix_login

class DetailsAdmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(Marolix_login,DetailsAdmin)