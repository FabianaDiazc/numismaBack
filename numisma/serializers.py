from numisma.models import Usuario
from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    """
        Usuario serializer class 
        The base model is user for easier serialization
    """
    username = serializers.CharField(source = 'user.username')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    password = serializers.CharField(source = 'user.password', required = False)

    class Meta:
        model = Usuario
        fields  = fields = ('id', 'username', 'first_name', 'last_name', 'genero', 'numentradas', 'password')