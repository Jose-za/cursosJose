"""cursoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Principal import views
from django.conf import settings
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que almacenan la ubicación de nuestras imagenes 
from cursos import views as views_cursos
#Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_cursos.cursos, name="Principal"),
    path('cursos/',views.cursos, name="Cursos"),
    path('contacto/',views.contacto, name="Contacto"),

    path('eliminarCurso/<int:i>/',views_cursos.eliminarCurso,name='Eliminar'),
    path('ActualizarCurso/<int:i>/', views_cursos.consultarCurso, name='ConsultarIndividual'),
    path('editarCurso/<int:i>/', views_cursos.editarCurso, name='Editar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)