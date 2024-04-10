from django.shortcuts import render
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'compra/nuevo_proveedor.html', {'form': form})

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'compra/nuevo_producto.html', {'form': form})