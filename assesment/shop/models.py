from django.db import models

# Create your models here.
class adminmaster(models.Model):
    id=models.AutoField(primary_key=True)
    adminid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.adminid
class customer(models.Model):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    useraddress=models.CharField(max_length=50)
    userphone=models.CharField(max_length=10)
    useremail=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
class eventdetails(models.Model):
    eventid=models.AutoField(primary_key=True)
    eventname=models.CharField(max_length=30)
    eventdesc=models.CharField(max_length=50)
    eventprice=models.IntegerField(default=None)
    eventqty=models.IntegerField(default=None)
    eventimage=models.ImageField(upload_to='images/')
    
class ordermaster(models.Model):
    ordereventid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(customer,on_delete=models.CASCADE)
    dateoforderevent=models.DateField(auto_now=True)
    ordereventstatus=models.CharField(max_length=30)
    eid=models.ForeignKey(eventdetails,default=None,on_delete=models.CASCADE)
    eventquantity=models.IntegerField(default=None)
    
