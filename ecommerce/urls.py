from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # App tienda
    path("", include("tienda.urls")),

    # Login / Logout Django
    path("accounts/", include("django.contrib.auth.urls")),
]
