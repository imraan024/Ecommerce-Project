from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    context = {}
    products = Products.objects.get_queryset().order_by('id')
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products' : page_obj,
        'page_obj' : page_obj
    }
    return render(request, "home.html", context)
