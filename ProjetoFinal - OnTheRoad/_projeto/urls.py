"""_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import  static
from .settings import MEDIA_URL, MEDIA_ROOT
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from carro.views import principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name='home'),
    path('', include('carro.urls')),
    path('', include('accounts.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('equipe/', auth_views.LoginView.as_view(), name='equipe'),
    path('krysllane/', auth_views.LoginView.as_view(), name='krysllane'),
    path('gabriel/', auth_views.LoginView.as_view(), name='gabriel'),
    path('adilson/', auth_views.LoginView.as_view(), name='adilson'),
    path('larissa/', auth_views.LoginView.as_view(), name='larissa'),
    path('mark/', auth_views.LoginView.as_view(), name='mark'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inicial/', auth_views.LogoutView.as_view(), name='inicial'),
    
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)