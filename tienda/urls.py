from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    # Navegación
    path("", views.inicio, name="inicio"),
    path("panel/", views.panel, name="panel"),
    path("registro/", views.registro, name="registro"),

    # Productos
    path("productos/", views.listar_productos, name="listar_productos"),
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),

    # 🛒 Carrito
    path("carrito/", views.ver_carrito, name="ver_carrito"),
    path("carrito/agregar/<int:id>/", views.agregar_carrito, name="agregar_carrito"),
    path("carrito/eliminar/<int:id>/", views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path("carrito/checkout/", views.checkout, name="checkout"),
]