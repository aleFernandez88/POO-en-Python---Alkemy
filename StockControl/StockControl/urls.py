from django.contrib import admin
from django.urls import path
from compra import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('productos/',views.productos, name="productos"),
    path('productos/agregarProducto', views.agregarProducto, name='agregarProducto'),
    path('productos/eliminarProducto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('productos/editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('productos/editado', views.editar, name='editado'),
    path('proveedores/',views.proveedores, name="proveedores"),
    path('proveedores/agregarProveedor', views.agregarProveedor, name='agregarProveedor'),
    path('proveedores/eliminarProveedor/<int:id>', views.eliminarProveedor, name='eliminarProveedor'),
    path('proveedores/editarProveedor/<int:id>', views.editarProveedor, name='editarProveedor'),
    path('proveedores/editadoPro', views.editar, name='editadoPro'),
]
