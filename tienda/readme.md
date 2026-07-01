# E-commerce Django - Proyecto Final

 Descripción

Este proyecto corresponde a un e-commerce desarrollado con Django como parte de un proceso formativo.  
Permite la gestión de productos, carrito de compras y generación de órdenes asociadas a usuarios autenticados.

El sistema implementa un flujo completo:

**Catálogo → Carrito → Checkout (Compra)**

---

## Funcionalidades

###  Autenticación
- Registro de usuarios
- Inicio de sesión / cierre de sesión (Django auth)
- Acceso protegido al checkout

---

### Gestión de productos (Administrador)
- Crear productos
- Editar productos
- Eliminar productos
- Asignación de categorías
- Control de stock

---

###  Catálogo
- Listado de productos desde base de datos
- Visualización de nombre, descripción, precio y stock
- Botón para agregar productos al carrito

---

### Carrito de compras
- Agregar productos al carrito
- Eliminar productos del carrito
- Manejo mediante sesiones
- Cálculo de subtotal y total

---

### Checkout
- Creación de orden asociada al usuario
- Registro de productos comprados (OrderItem)
- Cálculo de total de compra
- Limpieza del carrito luego de la compra

---

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- Bootstrap 4
- CSS

---

## Instalación

2. Crear entorno virtual
python -m venv venv

Activar:

Windows:

venv\Scripts\activate

3. Instalar dependencias

pip install django

4. Migraciones

python manage.py makemigrations
python manage.py migrate

5. Crear superusuario

python manage.py createsuperuser

6. Ejecutar servidor

python manage.py runserver

Usuarios de prueba

Admin
Usuario: admin
Password: admin123 (ejemplo)

Cliente
Usuario: cliente
Password: cliente123 (ejemplo)

 Rutas principales
/ → Inicio
/productos/ → Catálogo
/carrito/ → Carrito
/carrito/checkout/ → Confirmación de compra
/admin/ → Panel administrador

 Modelos principales

Categoria
Producto
Order
OrderItem
Autor

Proyecto desarrollado como parte de formación en Django.

 Notas
El carrito funciona con sesiones
Las órdenes se guardan en base de datos
Proyecto tipo MVP funcional de e-commerce

### 1. Clonar repositorio
```bash
git clone  konaggro/portafolio-ecommerce

