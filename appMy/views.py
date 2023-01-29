from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request,'index.html',context)

def productCategory(request):
    context={}
    return render(request,'category.html',context)

def productAll(request):
    context={}
    return render(request,'products.html',context)

def Clients(request):
    context={}
    return render(request,'clients.html',context)

def Contact(request):
    context={}
    return render(request,'contact.html',context)