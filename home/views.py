from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse
from .models import Product
from home.forms import ProductForm

def home_view(request):
	products = Product.objects.all()
	context = {"products":products}
	return render(request, "product_list.html", context)

def add_product(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save() 
		return HttpResponseRedirect(reverse("home:main"))
	return render(request, "form.html", {"form":form} )

def edit_product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	form = ProductForm(request.POST or None, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:main"))
	return render(request, "form.html", {"form":form} )


