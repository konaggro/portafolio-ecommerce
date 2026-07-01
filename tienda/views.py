from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Producto, Order, OrderItem
from .forms import ProductoForm


# ==========================
# CRUD PRODUCTOS
# ==========================

def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, "tienda/listar_productos.html", {
        "productos": productos
    })


def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect("tienda:listar_productos")

    else:
        formulario = ProductoForm()

    return render(request, "tienda/formulario_producto.html", {
        "formulario": formulario
    })


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        formulario = ProductoForm(request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto actualizado correctamente.")
            return redirect("tienda:listar_productos")

    else:
        formulario = ProductoForm(instance=producto)

    return render(request, "tienda/formulario_producto.html", {
        "formulario": formulario
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect("tienda:listar_productos")

    return render(request, "tienda/confirmar_eliminacion.html", {
        "producto": producto
    })


# ==========================
# NAVEGACIÓN
# ==========================

def inicio(request):
    return render(request, "tienda/inicio.html")


def panel(request):
    return render(request, "tienda/panel.html")


# ==========================
# REGISTRO / LOGIN
# ==========================

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario creado correctamente.")
            return redirect("tienda:listar_productos")

    else:
        form = UserCreationForm()

    return render(request, "tienda/registro.html", {
        "form": form
    })


# ==========================
# CARRITO (SESSION)
# ==========================

def agregar_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)

    carrito = request.session.get("carrito", {})
    carrito[str(id)] = carrito.get(str(id), 0) + 1

    request.session["carrito"] = carrito

    messages.success(request, f"{producto.nombre} agregado al carrito")
    return redirect("tienda:listar_productos")


def ver_carrito(request):
    carrito = request.session.get("carrito", {})

    productos = Producto.objects.filter(id__in=carrito.keys())

    items = []
    total = 0

    for p in productos:
        cantidad = carrito[str(p.id)]
        subtotal = p.precio * cantidad
        total += subtotal

        items.append({
            "producto": p,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

    return render(request, "tienda/carrito.html", {
        "items": items,
        "total": total
    })


def eliminar_del_carrito(request, id):
    carrito = request.session.get("carrito", {})

    if str(id) in carrito:
        del carrito[str(id)]

    request.session["carrito"] = carrito

    messages.success(request, "Producto eliminado del carrito")
    return redirect("tienda:ver_carrito")


# ==========================
# CHECKOUT (ORDEN REAL)
# ==========================

@login_required
def checkout(request):
    carrito = request.session.get("carrito", {})

    if not carrito:
        messages.error(request, "El carrito está vacío")
        return redirect("tienda:listar_productos")

    order = Order.objects.create(
        user=request.user,
        total=0
    )

    total = 0
    productos = Producto.objects.filter(id__in=carrito.keys())

    for p in productos:
        cantidad = carrito[str(p.id)]
        subtotal = p.precio * cantidad

        OrderItem.objects.create(
            order=order,
            product=p,
            quantity=cantidad,
            price=p.precio
        )

        total += subtotal

        # (opcional pro) descontar stock
        p.stock -= cantidad
        p.save()

    order.total = total
    order.save()

    request.session["carrito"] = {}

    messages.success(request, "Compra realizada con éxito 🎉")
    return redirect("tienda:listar_productos")