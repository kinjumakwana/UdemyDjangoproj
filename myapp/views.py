from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,"myapp/index.html")

def Products(request):
    # products=["iphone","nokia","samsung"]
    # print("List of Products")    
    products = Product.objects.all()
    # list derive from database
    # return HttpResponse(products)
    context={'prod':products}
    return render(request,"myapp/index.html", context)

# class based view for above products view[ListView]
# class ProductListView(ListView):
#     model=Product
#     template_name="myapp/index.html"
#     context_object_name='prod'

def product_detail(request,id):
    products = Product.objects.get(id=id)
    context={'prod':products}
    return render(request,"myapp/productdetail.html", context)
    
    # return HttpResponse("Product id!: "+ str(id))

# class based view for above products detail view[DetailView]
# class ProductDetailView(DetailView):
#     model=Product
#     template_name="myapp/productdetail.html"
#     context_object_name='prod'

@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Product(name=name,price=price,desc=desc,images=image, seller_name=seller_name)
        product.save()
    return render(request,"myapp/addproduct.html")

# class based view for creating products[CreateView]
class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','desc','images','seller_name']
   
def update_product(request, id):
    products = Product.objects.get(id=id)
    if request.method == "POST":
        products.name = request.POST.get('name')
        products.price = request.POST.get('price')
        products.desc = request.POST.get('desc')
        products.images = request.FILES['upload']
        products.save()
        return redirect("/Products")
    context={'prod':products}
    return render(request,"myapp/updateproduct.html", context)

# class based view for Updating products[UpdateView()]
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','desc','images','seller_name']
    template_name_suffix='_update_form'

def delete_product(request, id):
    products = Product.objects.get(id=id)
    context={'prod':products}
    if request.method == "POST":
        products.delete()
        return redirect("/Products")
    return render(request,"myapp/delete.html", context)

# class based view for Deleting products[DeleteView()]
class ProductDeleteView(DeleteView):
    model = Product
    success_url=reverse_lazy('myapp:Products')

def mylistings(request):
    prod = Product.objects.filter(seller_name = request.user.id)
    context = {
                'products':prod,
    }   
    return render(request, 'myapp/mylistings.html',context)