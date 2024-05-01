from django.contrib import admin

from . import models

admin.site.register(models.ProductoCategoria)
admin.site.register(models.Precio)
admin.site.register(models.Producto)