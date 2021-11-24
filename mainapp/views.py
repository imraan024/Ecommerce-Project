from django.shortcuts import render
from .models import Products

# Create your views here.

def home_view(request):
    context = {}
    products = Products.objects.all()
    context['products'] = products
    return render(request, "home.html", context)