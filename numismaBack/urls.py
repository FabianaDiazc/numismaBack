"""numismaBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# VERY IMPORTANT, development ONLY, GUNICORN should not go upfront in production, NGINX should
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# end very important

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views as rest_views

from numisma.views import UsuarioDetail, UsuarioList, get_usuario_authenticated
from numisma.views import ObjetoDetail, ObjetoList
from numisma.views import AvatarDetail, AvatarList
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/usuarios/(?P<pk>[0-9]+)/$', UsuarioDetail.as_view(), name='usuario-detail'),
    url(r'^api/usuarios/$', UsuarioList.as_view()),
    url(r'^api/usuario/authenticated/$', get_usuario_authenticated),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token-auth/', rest_views.obtain_auth_token),
    url(r'^api/objetos/(?P<pk>[0-9]+)/$', ObjetoDetail.as_view()),
    url(r'^api/objetos/$', ObjetoList.as_view()),
    url(r'^api/avatars/(?P<pk>[0-9]+)/$', AvatarDetail.as_view()),
    url(r'^api/avatars/$', AvatarList.as_view()),
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# VERY IMPORTANT, development ONLY, GUNICORN should not go upfront in production, NGINX should
#urlpatterns += staticfiles_urlpatterns()
# end very important
