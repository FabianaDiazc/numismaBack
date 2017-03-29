from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Usuario(models.Model):
    """
        has a relationship with django user        
    """
    user = models.OneToOneField(User)
    # M | F
    genero = models.CharField(max_length=1)
    numentradas = models.IntegerField(blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        receiver that creates a token for every user
    """
    if created:
        Token.objects.create(user=instance)