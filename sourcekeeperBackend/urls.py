"""sourcekeeperBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token
from django.views.static import serve

from backend import views

urlpatterns = [
    url(r'sources/', include('backend.urls')),
    url(r'^auth/login', views.Login.as_view()),
    url(r'^auth/logout', views.Logout.as_view()),
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^auth/me', views.LoginCheck.as_view()),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^/?(?P<path>.*)?$', views.render_template),
]
