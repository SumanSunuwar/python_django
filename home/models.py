from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Seller(models.Model):
	name = models.CharField(max_length=255)
	contact = models.CharField(max_length=50,null=True, blank=True)
	adress = models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.CharField(max_length=100)
	pcode = models.CharField(max_length=100)
	category = models.CharField(max_length=255,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	Product_image = models.ImageField(upload_to="upload/product",null=True,blank=True)
	seller = models.ForeignKey(Seller, on_delete=CASCADE, null=True, blank=True)
	# is_for_sale = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



