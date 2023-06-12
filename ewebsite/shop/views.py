from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
import razorpay

@csrf_exempt
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
    thank = False
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        contact = Contact(name=name, email=email, surname=surname, subject=subject)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def product(request,id):
    product = Product.objects.filter(id=id)
    print(product)

    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Order(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        #paytm transfer request
        client = razorpay.Client(auth=("rzp_test_Rqo0bpQBzRSZzM", "bDghqI0n9toULtbq2IiDlfxS"))
        data = { "amount": int(amount)*100, "currency": "INR", "receipt": "order_rcptid_11" }
        print("data",data)
        payment = client.order.create(data=data)
        print("payemnt",payment)
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id, 'payment':payment})
    return render(request, 'shop/checkout.html')

def search(request):
    return render(request,'shop/search.html')



  
    
