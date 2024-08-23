from django.shortcuts import render, redirect
from .models import Product, Category, Cart,Order, OrderItem, Customer
from django.views.generic import ListView
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {
        "products": products
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, "store/category_list.html", {
        "categories": categories
    })

def shopping_cart(request):
    if request.user.is_authenticated:
        try:

            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            customer = Customer.objects.create(user=request.user, name=request.user.username, email=request.user.email)
        cart, created = Cart.objects.get_or_create(customer=customer)
        return render(request, "store/shopping_cart.html", {
        "cart": cart
    })
    else:
        return redirect('login')

def orders_view(request):
    if request.user.is_authenticated:
        try:

            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            customer = Customer.objects.create(user=request.user, name=request.user.username, email=request.user.email) 
        orders = Order.objects.filter(customer=customer)
        return render(request, "store/orders.html", {
        "orders": orders
    })
    else:
        return redirect('login')


def index(request):
    products = Product.objects.all()
    return render(request, "store/index.html", {
        "products": products
    })