from django.shortcuts import render,redirect
from django.contrib import messages
from buyer.models import *
from seller.models import *
from siteadmin.models import *
import datetime

# Create your views here.
def register(request):
    return render(request,'register.html')
def registerAction(request):
    nam=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    dob=request.POST['dob']
    coun=request.POST['country']
    phn=request.POST['phonenumber']
    usr=request.POST['username']
    pas=request.POST['password']
    buyer=register_tb(name=nam,address=add,gender=gen,dob=dob,country=coun,phonenumber=phn,username=usr,password=pas)
    buyer.save()
    messages.add_message(request,messages.INFO,"Registration Success")
    return redirect('register')
def buyerupdate(request):
    buy=request.session['id']
    buyer=register_tb.objects.filter(id=buy)
    return render(request,'buyerupdate.html',{'buy':buyer})
def buyerUpdateAction(request):
    updt=request.session['id']
    nam=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    dob=request.POST['dob']
    coun=request.POST['country']
    phn=request.POST['phonenumber']
    usr=request.POST['username']
    pas=request.POST['password']
    buyer=register_tb.objects.filter(id=updt).update(name=nam,address=add,dob=dob,country=coun,phonenumber=phn,username=usr,password=pas)
    messages.add_message(request,messages.INFO,"Your data updated")
    return redirect('buyerupdate')
def viewproducts(request):
    buyer=request.session['id']
    viewpro=product_tb.objects.all()
    return render(request,'viewproducts.html',{"view":viewpro})
def addtocart(request,id):
    product=product_tb.objects.filter(id=id)
    return render(request,'addtocart.html',{"buy":product})
def addToCartAction(request):
    shippingaddress=request.POST['shippingaddress']
    quantity=request.POST['quantity']
    phn=request.POST['phonenumber']
    totalprice=request.POST['totalprice']
    buyerid=request.session['id']
    proid=request.POST['productid']
    buyer=cart_tb(shippingaddress=shippingaddress,quantity=quantity,phonenumber=phn,totalprice=totalprice,buyerid_id=buyerid,productid_id=proid)
    buyer.save()
    return redirect('viewproducts')
def viewcart(request):
    buyer=request.session['id']
    viewpro=cart_tb.objects.filter(buyerid=buyer)
    return render(request,'viewcart.html',{"view":viewpro})
def deletecart(request,id):
    delete=cart_tb.objects.filter(id=id).delete()
    return redirect('viewcart')
def placeOrderAction(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    check=request.POST.getlist('checkbox')
    for cid in check:
        cartitem=cart_tb.objects.filter(id=cid)
        stock=cartitem[0].productid.stock
        shippingaddress=cartitem[0].shippingaddress
        phonenumber=cartitem[0].phonenumber
        quantity=cartitem[0].quantity
        totalprice=cartitem[0].totalprice
        sellerid=cartitem[0].productid.sellerid
        productid=cartitem[0].productid
        buyerid=request.session['id']
    if quantity>int(stock):
        messages.add_message(request,messages.INFO,"out of stock")
        return redirect('viewcart')
    else:
        order=order_tb(date=date,time=time,shippingaddress=shippingaddress,phonenumber=phonenumber,quantity=quantity,totalprice=totalprice,sellerid=sellerid,productid=productid,buyerid_id=buyerid)
        order.save()
        messages.add_message(request,messages.INFO,"order placed")
        newstock=int(stock)-quantity
        product=product_tb.objects.filter(id=productid.id).update(stock=newstock)
        cartitem.delete()
    return redirect('viewcart')
def vieworder(request):
    buyer=request.session['id']
    orderview=order_tb.objects.filter(buyerid=buyer)
    return render(request,'vieworder.html',{"view":orderview})
def cancelorder(request,id):
    delorder=order_tb.objects.filter(id=id).update(status="canceled")
    return redirect('vieworder')    
def viewtracking(request,id):#tracking_tb's id
    track=tracking_tb.objects.filter(orderid=id)#checking the tracking table id specified order-id 
    return render(request,'viewtracking.html',{"view":track})
def searchproduct(request):
    return render(request,'searchproduct.html')
def searchAction(request):
    search=request.POST['searchproduct']
    product=product_tb.objects.filter(productname__istartswith=search)
    return render(request,'viewproducts.html',{"view":product})
def searchcategory(request):
    search=category_tb.objects.all()
    return render(request,'searchcategory.html',{"ser":search})
def searchCategoryAction(request):
    category=request.POST['category']
    price=request.POST['price']
    search=product_tb.objects.filter(price__lte=price,categoryid_id=category)
    return render(request,'viewproducts.html',{"view":search})
    
