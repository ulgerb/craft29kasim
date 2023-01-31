from django.shortcuts import render
from .models import *
from django.db.models import Q 
# Create your views here.


def index(request):
    context={"title":"Anasayfa"}
    products1 =Product.objects.all().order_by("?")[:3]
    category_e = Category.objects.get(title="Elektronik") 
    products_e = Product.objects.filter(category=category_e)
    
    category_k = Category.objects.get(title="Kıyafet")
    products_k = Product.objects.filter(category=category_k)
    
    if request.method == "POST":
        button = request.POST["button"]
        if button == "query":
            query = request.POST["q"]
            products = Product.objects.filter(
                Q(title__icontains=query) | Q(text__icontains=query) | Q(category__title__icontains=query))
            return render(request,'products.html', {"products":products})
        
    
    
    context.update({
        "products1": products1,
        "products_e": products_e,
        "products_k": products_k,
    })
    return render(request,'index.html',context)

def productCategory(request,categoryid="Elektronik"):
    context={"title":"Kategori"}
    category_k = Category.objects.get(title=categoryid)
    products = Product.objects.filter(category=category_k)
    category = Category.objects.all()
    
    context.update({
        "products": products,
        "categoryid": categoryid,
        "category": category,
    })
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