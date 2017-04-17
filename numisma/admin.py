from django.contrib import admin

# Register your models here.
from numisma.models import Usuario, Objeto, Avatar

class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, UsuarioAdmin)

class ObjetoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Objeto, ObjetoAdmin)

class AvatarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Avatar, AvatarAdmin)