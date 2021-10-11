from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import HttpResponse
from .models import Product
from home.forms import ProductForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
	print(request.user)
	products = Product.objects.all()
	context = {"products":products}
	return render(request, "product_list.html", context)

#create
class AddProductView(LoginRequiredMixin, CreateView):
	model = Product
	form_class = ProductForm
	template_name = "form.html"

		
	def get_success_url(self):
		return reverse("home:main")


def add_product(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save() 
		return HttpResponseRedirect(reverse("home:main"))# redirecting to a url
	return render(request, "form.html", {"form":form} )

def edit_product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	form = ProductForm(request.POST or None, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("home:main"))
	return render(request, "form.html", {"form":form} )


def delete_product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	product.delete()
	return redirect(reverse("home:main"))




