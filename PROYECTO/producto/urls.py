from django.urls import path
from . import views
app_name = "producto"

urlpatterns = [
    path("",views.home,name="Home"),
    path("productocategoria/create/",views.productocategoria_create,name="productocategoria_create"),
    path("productos_buscador_categoria/",views.home_1,name="buscador_productos"),
    
]