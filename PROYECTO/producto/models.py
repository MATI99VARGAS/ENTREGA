from django.db import models

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=200,unique=True)
    descripcion = models.CharField(max_length=250,null=True, blank=True,verbose_name='descripción')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "categoría de productos"

class Precio(models.Model):
    precio_unitario = models.PositiveBigIntegerField()
    def __str__(self):

     return self.precio_unitario

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200,unique=True)
    modelo_categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True, verbose_name="categoría de productos")
    precio_producto = models.ForeignKey(Precio, on_delete=models.SET_NULL, null=True, verbose_name="Precio")
    
    def __str__(self):

     return self.nombre
     
