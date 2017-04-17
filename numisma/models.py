from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Usuario(models.Model):
    """
        has a relationship with django user        
    """
    user = models.OneToOneField(User)
    # M | F
    genero = models.CharField(max_length=1)
    numentradas = models.IntegerField(blank=True)
    avatarRecta = models.ForeignKey('Avatar', related_name='avatar_recta', blank = True, null = True)
    avatarBalanza = models.ForeignKey('Avatar', related_name='avatar_balanza', blank = True, null = True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        receiver that creates a token for every user
    """
    if created:
        Token.objects.create(user=instance)

class Objeto(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField()
    valor = models.IntegerField()

class Avatar(models.Model):
    TYPE_CHOICES = (
        ('RECTA_NUMERICA', 'RECTA_NUMERICA'),
        ('BALANZA', 'BALANZA'),
        ('ANY', 'ANY'))

    imagen = models.ImageField()
    juego = models.CharField(max_length = 40, choices = TYPE_CHOICES)