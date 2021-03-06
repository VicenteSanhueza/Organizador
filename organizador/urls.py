"""organizador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth.views import LoginView

from apps.hogar.views import loginUser,Register

urlpatterns = [
    path('admin/', admin.site.urls),
    # Como añadir url de app
    #path('nombre_app/', include(('apps.nombre_app.urls','app_name'),namespace='nombre_app')),
    # Sitio para registrar usuario administrador y domicilio
    path('register/', Register.as_view(), name='register'),
    # Sitio para registrar usuario común en un domicilio
    path('login/', loginUser, name='login'),
    # Conservar así para luego añadir otros elementos de interfaz con menor importancia
    # Página de contacto, ayuda, etc.
    path('', include(('apps.interfaz.urls','app_name'),namespace='interfaz')),
    path('hogar/', include(('apps.hogar.urls','app_name'),namespace='hogar')),
    path('tareas/', include(('apps.tareas.urls','app_name'),namespace='tareas')),
    path('calendario/', include(('apps.almanac_calendar.urls','app_name'), namespace='calendario')),
]
