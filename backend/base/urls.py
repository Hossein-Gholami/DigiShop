from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:product_id>/', views.getProduct, name="product"),
]
