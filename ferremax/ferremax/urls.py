"""
URL configuration for ferremax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ferremax_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('registrar/',views.registrar, name ='registrar'),
    path('tasks/',views.tasks, name ='tasks'),
    path('logout/',views.cerrar_sesion, name ='logout'),
    path('ingresar/',views.ingresar, name ='ingresar'),
    path('ingresarproductos/',views.ingresar_productos, name ='ingresarproductos'),
    path('modificarproducto/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminarproducto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('listaproductos/', views.lista_productos, name='lista_productos'),
]