from django.shortcuts import render,redirect
from seller.models import *
from buyer.models import *
from siteadmin.models import *
from django.contrib import messages
import datetime


# Create your views here.
def sellerregister(request):
    return render(request,'sellerregister.html')
def sellerRegisterAction(request):
    name=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    dob=request.POST['dob']
    coun=request.POST['country']
    phn=request.POST['phonenumber']
    usr=request.POST['username']#name taken from html page
    pas=request.POST['password']
    if  len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img="nopic"
    seller=sellerregister_tb(name=name,address=add,gender=gen,dob=dob,country=coun,phonenumber=phn,username=usr,password=pas,image=img)#name from database
    seller.save()
    return redirect('sellerregister')
def sellerupdate(request):
    sell=request.session['id']
    seller=sellerregister_tb.objects.filter(id=sell)
    return render(request,'sellerupdate.html',{"sell":seller})
def sellerUpdateAction(request):
    updt=request.session['id']
    seller=sellerregister_tb.objects.filter(id=updt)
    name=request.POST['name']
    add=request.POST['address']
    gen=request.POST['gender']
    dob=request.POST['dob']
    coun=request.POST['country']
    phn=request.POST['phonenumber']
    usr=request.POST['username']
    pas=request.POST['password']    
    if len(request.FILES)>0:
        varfile=request.FILES['file']
    else:
        varfile=seller[0].image
    seller=sellerregister_tb.objects.filter(id=updt).update(name=name,address=add,gender=gen,dob=dob,country=coun,phonenumber=phn,username=usr,password=pas)
    seller_obj=sellerregister_tb.objects.get(id=updt)
    seller_obj.image=varfile
    seller_obj.save()
    return redirect('sellerupdate')
def addproduct(request):
    product=category_tb.objects.all()
    return render(request,'addproduct.html',{"addproduct":product})
def addProductAction(request):
    proname=request.POST['productname']
    if len(request.FILES)>0:
       file=request.FILES['file']
    else:
        file="nopic"
    stock=request.POST['stock']
    price=request.POST['price']
    details=request.POST['details']
    catid=request.POST['category']
    sellid=request.session['id']    
    seller=product_tb(productname=proname,file=file,stock=stock,price=price,details=details,categoryid_id=catid,sellerid_id=sellid)
    seller.save()
    messages.add_message(request,messages.INFO,"New product added")
    return redirect('addproduct')
def sellerProductView(request):
    seller=request.session['id']
    seller=product_tb.objects.filter(sellerid=seller)
    return render(request,'sellerProductView.html',{"view":seller})
def deleteproduct(request,id):                                                                                           
    dele=product_tb.objects.filter(id=id).delete()
    return redirect('sellerProductView')
def updateproduct(request,id):
    edit=product_tb.objects.filter(id=id)
    cat=category_tb.objects.all()
    return render(request,'updateproduct.html',{"updt":edit,"cate":cat})
def updateProductAction(request):
    sellid=request.session['id']
    productid=request.POST['uid']
    product=product_tb.objects.filter(id=productid)
    proname=request.POST['productname']
    if len(request.FILES)>0:
        file=request.FILES['file']
    else:
        file=product[0].file
    stock=request.POST['stock']
    price=request.POST['price']
    details=request.POST['details']
    cat=request.POST['category']
    product=product_tb.objects.filter(id=productid).update(productname=proname,stock=stock,price=price,details=details,categoryid_id=cat,sellerid_id=sellid)
    product_obj=product_tb.objects.get(id=productid)
    product_obj.file=file
    product_obj.save()
    return redirect('sellerProductView')
def vieworderseller(request):
    seller=request.session['id']
    orderview=order_tb.objects.filter(sellerid=seller)
    return render(request,'vieworderseller.html',{"view":orderview})
def approveorder(request,id):
    seller=order_tb.objects.filter(id=id).update(status="approved")
    return redirect('vieworderseller')
def rejectorder(request,id):
    seller=order_tb.objects.filter(id=id).update(status="rejected")
    return redirect('vieworderseller')
def tracking(request,id):
    seller=order_tb.objects.filter(id=id)
    return render(request,'tracking.html',{"track":seller})
def trackingAction(request):
    orderid=request.POST['orderid']#order id getting by POST from html page tracking.html hidden
    track=order_tb.objects.get(id=orderid)
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    track1=tracking_tb(orderid=track,details=details,date=date,time=time)
    track1.save()
    return render(request,'tracking.html')
def confirmreject(request,id):
    reject=order_tb.objects.filter(id=id)
    reject.update(status="confirmreject")
    stock=reject[0].productid.stock
    quantity=reject[0].quantity
    stock=int(stock)+quantity
    confirm=product_tb.objects.filter(id=reject[0].productid.id)
    confirm.update(stock=stock)
    return redirect('vieworderseller')
    
    
    
    
        
    
