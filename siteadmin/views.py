from django.shortcuts import render,redirect
from siteadmin.models import *
from seller.models import *
from buyer.models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    usr=request.POST['username']
    pas=request.POST['password']
    siteadmin=admin_tb.objects.filter(username=usr,password=pas)
    buyer=register_tb.objects.filter(username=usr,password=pas)
    seller=sellerregister_tb.objects.filter(username=usr,password=pas)
    if  siteadmin.count()>0:
        request.session['id']=siteadmin[0].id
        return render(request,'adminhome.html')
    elif buyer.count()>0:
         request.session['id']=buyer[0].id
         return render(request,'buyerhome.html')
    elif seller.count()>0:
         status=seller[0].status
         if status=="approved":
             request.session['id']=seller[0].id
             return render(request,'sellerhome.html')
         else:
             messages.add_message(request,messages.INFO,"login failed")
             return render(request,'login.html')
    else:
         messages.add_message(request,messages.INFO,"login failed")
         return render(request,'login.html')
def sellerregisterview(request):
    #admin=request.session['id']
    view=sellerregister_tb.objects.all()
    return render(request,'sellerregisterview.html',{"admin":view})
def approved(request,id):
    admin=sellerregister_tb.objects.filter(id=id).update(status="approved")
    return redirect('sellerregisterview')
def category(request):
    return render(request,'category.html')
def categoryAction(request):
    name=request.POST['name']
    siteadmin=category_tb(name=name)
    siteadmin.save()
    messages.add_message(request,messages.INFO,"New category added")
    return redirect('category')
def checkusername(request):
    username=request.GET['sid']
    siteadmin=admin_tb.objects.filter(username=username)
    buyer=register_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    
    if len(siteadmin)>0:
        msg="exist"
    elif len(buyer)>0:
        msg="exist"
    elif len(seller)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({"valid":msg})
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotpasswordAction(request):
    usr=request.POST['username']
    seller=sellerregister_tb.objects.filter(username=usr)
    buyer=register_tb.objects.filter(username=usr)
    if  seller.count()>0:
        request.session['id']=seller[0].id
        return render(request,'newpassword.html',{"data":usr})
    elif buyer.count()>0:
         request.session['id']=buyer[0].id
         return render(request,'newpassword.html',{"data":usr})
    else:
        return redirect('index')
def newPasswordAction(request):
    usr=request.POST['username']
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    seller=sellerregister_tb.objects.filter(name=name,dob=dob,country=country)
    buyer=register_tb.objects.filter(name=name,dob=dob,country=country)
    if  seller.count()>0:#checking the person is exist in tb(seller->var used to filter from tb)
        request.session['id']=seller[0].id
        return render(request,'changepassword.html',{"data":usr})
    elif buyer.count()>0:
         request.session['id']=buyer[0].id
         return render(request,'changepassword.html',{"data":usr})
    else:
        return render(request,'newpassword.html')
def changePasswordAction(request):
    usr=request.POST['username']
    newpas=request.POST['newpassword']
    conpas=request.POST['confirmpassword']
    seller=sellerregister_tb.objects.filter(username=usr)
    buyer=register_tb.objects.filter(username=usr)
    if  newpas==conpas:
        #seller=sellerregister_tb.objects.filter(username=usr)
        #buyer=register_tb.objects.filter(username=usr)
        if  seller.count()>0: 
            request.session['id']=seller[0].id
            sellerid=request.session['id']
            sell=sellerregister_tb.objects.filter(id=sellerid).update(password=newpas)
        else:
             
             request.session['id']=buyer[0].id
             buyerid=request.session['id']
             buy=register_tb.objects.filter(id=buyerid).update(password=newpas)
        return render(request,'changepassword.html')
    else:
        return redirect('index')
def logout(request):
    request.session.flush()
    return render(request,'index.html')
    

    
