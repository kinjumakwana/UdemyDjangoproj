from django.urls import path
from .views import *
app_name = 'myapp'
urlpatterns = [
    
    path('',index),
    path('Products/',Products, name="Products"),
    path('Productss/',ProductListView.as_view(), name="ProductListView"),

    # path('Products/<int:id>',product_detail, name="product_detail"),
    path('Products/<int:pk>',ProductDetailView.as_view(), name="product_detail"),
    
    # path('Products/add',add_product, name="add_product"),
    path('Products/add',ProductCreateView.as_view(), name="ProductCreateView"),
    
    # path('Products/update/<int:id>',update_product, name="update_product"),
    path('Products/update/<int:pk>',ProductUpdateView.as_view(), name="ProductUpdateView"),

    # path('Products/delete/<int:id>',delete_product, name="delete_product"),
    path('Products/delete/<int:pk>',ProductDeleteView.as_view(), name="ProductDeleteView"),
    
    path('Products/mylistings/',mylistings, name="mylistings"),
]
