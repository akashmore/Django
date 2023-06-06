from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

def index(request):
    products = Product.objects.all()
    n = len(products)
    nslides = n//3 + ceil((n/3)-(n//3))
    print(nslides)
    params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        contact = Contact(name=name, email=email, surname=surname, subject=subject)
        contact.save()
    return render(request,'shop/contact.html')

def tracking(request):
    return render(request,'shop/tracker.html')

def product(request,id):
    product = Product.objects.filter(id=id)
    print(product)

    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')

def search(request):
    return render(request,'shop/search.html')
    
