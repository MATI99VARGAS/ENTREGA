from django.shortcuts import render, redirect
from django import forms
from . import models, forms

def home(request):
    consulta_cliente = models.cliente.objects.all()
    context = {"clientes":consulta_cliente}
    return render(request,"cliente/index.html",context)

def cliente_create(request):
    if request.method == "POST":
        form = forms.Clientes_form(request.POST)
        form.save() 
        return redirect("cliente:Home")
    else:
        form = forms.Clientes_form()
    return render(request, "cliente/cliente_create.html",context={"form":form})
 