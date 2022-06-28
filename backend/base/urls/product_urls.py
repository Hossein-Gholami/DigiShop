from django.urls import path
from base.views import product_views as views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )

urlpatterns = [
    path('', views.getProducts, name="products"),
    path('<str:product_id>/', views.getProduct, name="product"),
]