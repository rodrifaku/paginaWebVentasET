from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from m_usuario.urls import urlpatterns as urlUsuario
from m_venta.urls import urlpatterns as urlVenta

from .views import (
    mostrar_principal,
    mostrar_productos,

)

urlpatterns = [
    path('', mostrar_principal, name='mostrar_principal'),
    path('productos/', mostrar_productos, name='mostrar_productos'),
    path('', include('m_usuario.urls')),  # 1 opción
    path('', include('m_venta.urls')),
    path('admin/', admin.site.urls),


]
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
