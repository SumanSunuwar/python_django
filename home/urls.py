from home.views import add_product, home_view, edit_product
from django.urls import path

app_name = "home"

urlpatterns = [
    path("main/", home_view, name="main"),
    path("add_product/", add_product, name="add_product"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
]

