from home.models import Product
from django import forms
from django.db.models import fields

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     pcode = forms.CharField()
#     price = forms.CharField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name","pcode","description","price","category","seller","Product_image")
