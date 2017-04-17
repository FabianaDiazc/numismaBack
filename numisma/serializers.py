from numisma.models import Usuario, Objeto, Avatar
from django.contrib.auth.models import User
from rest_framework import serializers

class AvatarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Avatar
        fields  = fields = ('id', 'imagen', 'juego')

class UsuarioDTOSerializer(serializers.Serializer):
    username = serializers.CharField(source = 'user.username')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    password = serializers.CharField(source = 'user.password', required = False)
    avatar_recta = serializers.CharField()
    avatar_balanza = serializers.CharField()
    genero = serializers.CharField()
    password = serializers.CharField()

class UsuarioSerializer(serializers.ModelSerializer):
    """
        Usuario serializer class 
        The base model is user for easier serialization
    """
    username = serializers.CharField(source = 'user.username')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    password = serializers.CharField(source = 'user.password', required = False)
    avatarRecta = AvatarSerializer(many=False, read_only=True)
    avatarBalanza = AvatarSerializer(many=False, read_only=True)

    class Meta:
        model = Usuario
        fields  = fields = ('id', 'username', 'first_name', 'last_name', 'genero', 'numentradas', 'password', 'avatarRecta', 'avatarBalanza')

class ObjetoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Objeto
        fields  = fields = ('id', 'nombre', 'imagen', 'valor')