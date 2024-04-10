from django.contrib import admin
from .models import Producto
from .models import Proveedor

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
     list_display = ["nombre","precio","stock_actual"]
     
class ProveedorAdmin(admin.ModelAdmin):
     list_display = ["nombre","apellido","dni"]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)