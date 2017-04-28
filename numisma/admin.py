from django.contrib import admin

# Register your models here.
from numisma.models import Usuario, Objeto, Avatar, Juego, Puntaje, Nivel

class UsuarioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Usuario, UsuarioAdmin)

class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'valor')
admin.site.register(Objeto, ObjetoAdmin)

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'juego', 'imagen')
admin.site.register(Avatar, AvatarAdmin)

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'usuario')
admin.site.register(Juego, JuegoAdmin)

class PuntajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'juego', 'nivel')

admin.site.register(Puntaje, PuntajeAdmin)

class NivelAdmin(admin.ModelAdmin):
     list_display = ('id', 'nombre', 'tipo')
admin.site.register(Nivel, NivelAdmin)