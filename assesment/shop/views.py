from django.shortcuts import render,redirect
from django.http import JsonResponse
from.models import adminmaster,eventdetails,customer,ordermaster

# Create your views here.
def home(request):
    return render(request,'home.html')
def adminlog(request):
    if request.method=='POST':
        adminid=request.POST.get('adminid')
        password=request.POST.get('password')     
        obj= adminmaster.objects.get( adminid=adminid,password=password)
        return redirect('/adminlanding')
    return render(request,'adminlog.html')
def userlog(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj= customer.objects.get(useremail=username,password=password)
        request.session['userid']=obj.userid
        return redirect('/customerlanding')
    return render(request,'userlog.html')
def userreg(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        obj=customer.objects.create(username=name,useraddress=address,useremail=email,userphone=phone,password=password)
        obj.save()
        return redirect('/userlog')
    return render(request,'userreg.html')
def adminlanding(request):
    return render(request,'adminlanding.html')
def customerlanding(request):
    return render(request,'customerlanding.html')
def enterevent(request):
    if request.method=='POST':
        eventname=request.POST['eventname']
        eventdesc=request.POST['eventdesc']
        eventqty=request.POST['eventqty']
        eventprice=request.POST['eventprice']
        # eventimage=request.FILES['eventimage']
        obj=eventdetails.objects.create(eventname=eventname,eventdesc=eventdesc,
                                          eventqty=eventqty,eventprice=eventprice)
        obj.save()
        return redirect('/event')
        #return redirect('/adminlanding',{'message':'product added successfully'})
    obj=eventdetails.objects.all()
    return render(request,'event.html',{'event':obj})
def showevent(request):
    obj=eventdetails.objects.all()
    return render(request,'showevent.html',{'event':obj})
def deleteevent(request,eventid):
    obj=eventdetails.objects.get(pk=int(eventid))
    obj.delete()
    obj=eventdetails.objects.all()
    return redirect('/products')
def editevent(request,eventid):
    if request.method=='POST':
        eventid=request.POST['eventid']
        eventname=request.POST['eventname']
        eventdesc=request.POST['eventdesc']
        eventqty=request.POST['eventqty']
        eventprice=request.POST['eventprice']
        eventimage=request.FILES['eventimage']
        obj=eventdetails.objects.get(pk=int(eventid))
        obj.eventname=eventname
        obj.eventdesc=eventdesc
        obj.eventqty=eventqty
        obj.eventprice=eventprice
        obj.eventtimage=eventimage
        obj.save()
        return redirect('/events')
    obj=eventdetails.objects.get(pk=int(eventid))
    return render(request,'editevent.html',{'eventid':obj.eventid,'eventname':obj.eventname,'eventdesc':obj.eventdesc,'eventprice':obj.eventprice,'eventimage':obj.eventimage,'eventqty':obj.eventqty})
def orderevent(request,pk):
    if request.method=='POST':
        userid=customer.objects.get(pk=int(request.POST['userid']))
        eid=eventdetails.objects.get(pk=int(pk))
        eventquantity=request.POST['eventqty']
        ordermaster.objects.create(userid=userid,eid=eid, eventquantity = eventquantity ,ordereventstatus='under process')
        return redirect('/customerlanding')
    obj=eventdetails.objects.get(pk=int(pk))
    eventquantity=int(obj.eventqty)+1
    quantity_range=range(1,eventquantity)
    return render(request,'orderevent.html',{'events':obj,'quantity_range':quantity_range})
def showeventorder(request):
    userid=request.session['userid']
    obj=ordermaster.objects.filter(userid=userid)
    return render(request,'showeventorder.html',{'orders':obj})
def allevent(request):
    obj=ordermaster.objects.all()
    return render(request,'allevent.html',{'orders':obj})
def changestatus(request,orderid):
    if request.method=='POST':
        obj=ordermaster.objects.get(pk=int(orderid))
        obj.orderstatus=request.POST['orderstatus']
        obj.save()
        return redirect('/allevent')
    obj=ordermaster.objects.get(pk=int(orderid))
    return render(request,'changestatus.html',{'orderstatus':obj.orderstatus})
def cancelorderevent(request,ordereventid):
    obj=ordermaster.objects.get(pk=int(ordereventid))
    obj.delete()
    return redirect('/customerlanding')
def logout(request):
    request.session.flush()
    return redirect('/')
def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        new_password = request.POST['new_password']
        obj=customer.objects.get(useremail=email,userphone=phone)
        obj.password=new_password
        obj.save()
        return redirect('/userlog')
    return render(request,'forgot_password.html')