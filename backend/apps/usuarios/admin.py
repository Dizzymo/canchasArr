from django.contrib import admin
from .models import   User  

# Register your models here.

# class CustomUserAdmin(UserAdmin):

    # Campos a mostrar en la vista de detalle del usuario
    # exclude = ('first_name',)
 
admin.site.register(User)
 