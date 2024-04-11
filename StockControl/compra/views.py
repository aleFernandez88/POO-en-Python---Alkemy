from django.shortcuts import render, redirect
from compra.models import Producto,Proveedor
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, "main.html")


def productos(request):
    productos = Producto.objects.all()
    return render(
        request,
        "productos.html",
        {'productos': productos}
    )


def agregarProducto(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    stock = request.POST["stock_actual"]
    p = Producto(nombre=nombre, precio=precio, stock_actual=stock)
    p.save()
    messages.success(request, 'Producto agregado.')
    return redirect('productos')


def eliminarProducto(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado.')
    return redirect('productos')


def editarProducto(request, id):
    producto = Producto.objects.get(pk=id)
    return render(
        request,
        'productoEditar.html',
        {'producto': producto}
    )


def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    stock = request.POST["stock_actual"]
    id = request.POST['id']
    Producto.objects.filter(pk=id).update(
        id=id, nombre=nombre,
        precio=precio,
        stock_actual=stock
    )
    messages.success(request, 'Producto actualizado.')
    return redirect('productos')

# --------------------------------------------------------------------------

def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(
        request,
        "proveedores.html",
        {'proveedores': proveedores}
    )


def agregarProveedor(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    p = Proveedor(nombre=nombre, apellido=apellido, dni=dni)
    p.save()
    messages.success(request, 'Proveedor agregado.')
    return redirect('proveedores')


def eliminarProveedor(request, id):
    proveedor = Proveedor.objects.filter(pk=id)
    proveedor.delete()
    messages.success(request, 'Proveedor eliminado.')
    return redirect('proveedor')


def editarProveedor(request, id):
    proveedor = Proveedor.objects.get(pk=id)
    return render(
        request,
        'proveedorEditar.html',
        {'proveedor': proveedor}
    )


def editarPro(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    id = request.POST['id']
    Proveedor.objects.filter(pk=id).update(
        id=id, nombre=nombre,
        apellido=apellido,
        dni=dni
    )
    messages.success(request, 'Proveedor actualizado.')
    return redirect('proveedores')
