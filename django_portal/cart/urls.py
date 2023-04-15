from django.urls import path, include
from . import views

urlpatterns = [
    path('add/<int:product_id>', views.cart_add, name='cart_add'),
    path('', views.cart_detail, name='cart_detail'),
]