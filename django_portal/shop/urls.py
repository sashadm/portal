from django.urls import path, include
from .views import *

urlpatterns = [
    path('section/<int:id>', show_section),
    path('rubric/<int:id>', show_rubric),
    path('product/<int:id>', show_product),
    path('', index),
]
