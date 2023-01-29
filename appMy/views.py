from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    context={"title":"Anasayfa"}
    products1 =Product.objects.all().order_by("?")[:3]
    category_e = Category.objects.get(title="Elektronik") 
    products_e = Product.objects.filter(category=category_e)
    
    context.update({
        "products1": products1,
        "products_e": products_e,
    })
    return render(request,'index.html',context)

def productCategory(request):
    context={}
    return render(request,'category.html',context)

def productAll(request):
    context={"title": "Tüm Ürünler"}
    
    products = Product.objects.all()
    
    context.update({"products": products})
    return render(request,'products.html',context)

def Clients(request):
    context={}
    return render(request,'clients.html',context)

def Contact(request):
    context={}
    return render(request,'contact.html',context)