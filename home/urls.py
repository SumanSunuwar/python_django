from home.views import add_product, home_view, edit_product, AddProductView
from django.urls import path

app_name = "home"

urlpatterns = [
    path("main/", home_view, name="main"),
    
    path("add_product/", AddProductView.as_view(), name="add_product"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
]

