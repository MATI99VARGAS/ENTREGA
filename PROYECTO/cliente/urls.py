from django.urls import path
from . import views
app_name = "cliente"

urlpatterns = [
    path("",views.home,name="Home"),
    path("cliente_create/",views.cliente_create,name="cliente_create"),
    
]