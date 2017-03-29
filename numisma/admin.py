from django.contrib import admin

# Register your models here.
from numisma.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, UsuarioAdmin)