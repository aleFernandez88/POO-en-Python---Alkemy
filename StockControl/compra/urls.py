from django.urls import path
from . import views

urlpatterns = [
    path('nuevo-proveedor/', views.nuevo_proveedor),
    path('nuevo-producto/', views.nuevo_producto),
]