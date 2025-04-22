"""
URL configuration for parqueadero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    return redirect('/login/')

urlpatterns = [
    path('admin/login/', lambda request: redirect('login/')),
    path('admin/', admin.site.urls),
    path('', home_redirect),
    path('login/', include('login.urls')),
    path('',include('celda.urls')),
    path('', include(('cliente.urls', 'cliente'), namespace='cliente')),
    path('',include('pago.urls')),
    path('',include('vehiculo.urls')),
    path('',include('parqueo.urls')),
    path('',include('tarifa.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),

]
