from django.contrib import admin

from .models import Producto


# Register your models here.
class ProductoAdminArea(admin.AdminSite):
    site_header = 'Productos admin'


productos_sitio = ProductoAdminArea(name='ProductosAdmin')

admin.site.register(Producto)
productos_sitio.register(Producto)
