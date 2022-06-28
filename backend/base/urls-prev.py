from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = "base"

urlpatterns = [
    path('users/', views.getUsers, name="users"),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('users/register/', views.registerUser, name="register"),
    path('users/profile/', views.getUserProfile, name="users_profile"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:product_id>/', views.getProduct, name="product"),
    path('', views.getRoutes, name="routes"),
]
