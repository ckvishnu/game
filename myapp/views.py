
from django.shortcuts import redirect, render
from django.http import HttpResponse
from random import *
from django.db import models
from .models import Total
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'page.html')

def buttonclick2(request):
    totala=Total.objects.get(id='1')
    totala.total=0
    totala.save()
    return render(request,'page.html',{'msg':'Now roll the dice'})
    


def buttonclick(request):
    num=randint(1,6)
    
    totala=Total.objects.get(id='1')
    totala.total=totala.total + num
    b=totala.total
    totala.save()
    if totala.total >= 100:
        totala.total=0
        totala.save()
        messages.info(request,'CONGRATULATIONS')
        return redirect('/')
    if totala.total % 7 == 0:
        totala.total=0
        totala.save()
    
    return render(request,'page.html',{'msg1':b,'msg2':num})
    

