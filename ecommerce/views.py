from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
	products = Product.objects.all().filter(is_available = True)
	context = {'produits':products}
	return render(request, 'home.html', context)