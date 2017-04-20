from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from numisma.serializers import UsuarioSerializer, ObjetoSerializer, AvatarSerializer, UsuarioDTOSerializer
from numisma.serializers import NivelSerializer, PuntajeSerializer
from numisma.models import Usuario, Objeto, Avatar, Juego, Puntaje, Nivel
from numisma.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, status, generics
# two class based views.
class UsuarioList(APIView):
    permission_classes = (permissions.AllowAny, )
    """
        List all usuairos or create new usuario endpoint
    """
    def get(self, request, format = None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = UsuarioDTOSerializer(data = request.data)
        if serializer.is_valid():
            user = User(first_name = serializer.data['first_name'], \
                        last_name = serializer.data['last_name'],   \
                        username = serializer.data['username'])
            user.set_password(serializer.data['password'])
            user.save()
            usuario = Usuario(user = user, genero = serializer.data['genero'], numentradas = 0)
            avatarBalanza = Avatar.objects.filter(id = serializer.data['avatar_balanza']).first()
            avatarRecta = Avatar.objects.filter(id = serializer.data['avatar_recta']).first()
            usuario.avatarBalanza = avatarBalanza
            usuario.avatarRecta = avatarRecta
            usuario.save()
            self.create_juego(usuario)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def create_juego(self, usuario):
        juego = Juego(estado = 'EN_PROGRESO', usuario = usuario)
        juego.save()
        for currNivel in Nivel.objects.all():
            if currNivel.nombre == 'RECTA_NUMERICA' and currNivel.tipo == 'M':
                puntaje = Puntaje(estado = 'EN_PROGRESO', juego = juego, nivel = currNivel)
            else:
                puntaje = Puntaje(estado = 'BLOQUEADO', juego = juego, nivel = currNivel)
            puntaje.save()


class UsuarioDetail(APIView):
    """
        Retrieve, update or delete a usuario instance.
    """

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk = pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        usuario = self.get_object(pk)
        self.check_object_permissions(self.request, usuario)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        usuario = self.get_object(pk)
        self.check_object_permissions(self.request, usuario)
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = usuario.user
            user.first_name = serializer.data['first_name']
            user.last_name = serializer.data['last_name']
            user.save()
            usuario.genero = serializer.data['genero']
            usuario.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        usuario = self.get_object(pk)
        self.check_object_permissions(self.request, usuario)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_usuario_authenticated(request):
    """
    Devuelve la instancia de un usuario dado el token.
    """
    try:
        user = request.user
        usuario = Usuario.objects.filter(user__id__exact=user.id).first()
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['GET'])
def get_puntajes_usuario_juego_actual(request):
    """
    Devuelve la lista de puntajes del juego actual del usuario
    """
    try:
        user = request.user
        usuario = Usuario.objects.filter(user__id__exact=user.id).first()
        juego = Juego.objects.filter(usuario = usuario, estado = 'EN_PROGRESO').first()
        puntajes = juego.puntajes
        serializer = PuntajeSerializer(data = puntajes, many = True)
        if serializer.is_valid() == False:
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


class ObjetoList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer


class ObjetoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer

class AvatarList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

class AvatarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

class NivelList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer