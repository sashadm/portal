from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


def index(request):
    sections = Section.objects.all()
    return render(request, 'shop/index.html', {'sections': sections})


def show_section(request, id):
    section = get_object_or_404(Section, id=id)
    if request.method == 'GET':
        return render(request, 'shop/section.html', {'section': section})


def show_rubric(request, id):
    rubric = get_object_or_404(Rubric, id=id)
    if request.method == 'GET':
        return render(request, 'shop/rubric.html', {'rubric': rubric})


def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    if request.method == 'GET':
        return render(request, 'shop/product.html', {'product': product, 'cart_product_form': cart_product_form})



