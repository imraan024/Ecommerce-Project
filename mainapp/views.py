from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    context = {}
    products = Products.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products' : page_obj,
        'page_obj' : page_obj
    }
    return render(request, "home.html", context)

def login_view(request):
    return render(request, "login.html")

def registration_view(request):
    return render(request, "registration.html")