from django.shortcuts import render, redirect
from django import forms
from . import forms, models 

def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos":consulta_productos}
    return render(request,"producto/index.html",context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        form.save() 
        return redirect("producto:Home")
    else:
        form = forms.ProductoCategoriaForm()      
    return render(request, "Producto/productocategoria_create.html",context={"form":form})

