from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list, name="product_list"),
    path("categories/", views.category_list, name="category_list"),
    path("shopping_cart/", views.shopping_cart, name="shopping_cart"),
    path("orders/", views.orders_view, name="orders")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
