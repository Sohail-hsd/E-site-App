from django.db import reset_queries
from django.http import request, response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json

from .models import Product,mainImage,Contact,Order,updateOrder
from math import ceil, e

# Create your views here.

def test(request):
    return render(request,'Esite/test.html')

def index(request):
    allProds=[]
    Product_category = Product.objects.values('category','id')
    categorys = {item['category'] for item in Product_category }
    for cat in categorys:
        product = Product.objects.filter(category = cat)
        n= len(product)
        Slides= n//4 + ceil((n/4)-(n//4))
        allProds.append([product,range(1,Slides),Slides])

    # Main_Image_carousel
    image = mainImage.objects.all()
    params={'allProds':allProds,"image":image}
    
    return render(request,'Esite/index.html',params)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['massage']
        contact = Contact(name=name,email=email,phone=phone,description=msg)
        contact.save()
    return render(request,'Esite/contact.html')

def checkout(request):
    # Order Checkout Form.
    
    if request.method == 'POST':
        item_JSON = request.POST['item_JSON']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address1'] + " " + request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        print(f' {name} {email} {phone} {address} {city} {state} {zip_code} ')

        order = Order( item_JSON=item_JSON,email=email,name=name,phone=phone,address=address,city=city,zip_code=zip_code,state=state)
        order.save()
        thanks = True
        id=order.order_id
        update_Order = updateOrder(order_id=id,update_desc='Your Order is on the way!')
        update_Order.save()
        return render(request,'Esite/checkout.html',{'thanks':thanks,'id':id})
    return render(request,'Esite/checkout.html')

def about(request):
    return render(request,'Esite/about.html',{"page_name":"The About Page..!"})

def tracker(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        email = request.POST['email']
        #return HttpResponse(f'{order_id}  || {email}')

        try:
            order = Order.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update = updateOrder.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'date':item.timeStamp})
                    response = json.dumps([updates, order[0].item_JSON],default=str)
                    
                return HttpResponse(response)
            else:
                return HttpResponse('{}') # Empty is Handel in JavaScript...!
                ''' What happens if the Order id Or email is Not Correct...!'''
        except Exception as e:
            return HttpResponse('{}') # By default {}/ empty is handle in javaScript With a Sorry massage.
            ''' Exception Of the try block......! '''
    return  render(request,'Esite/tracker.html',{"page":"Tracker Page"})
        
def cart(request):
    return render(request,'Esite/cart.html',{"page":"The Cart Page"})
def product(request, myid):
    product=Product.objects.filter(id=myid).first()
    return render(request, "Esite/product.html", {'product':product})