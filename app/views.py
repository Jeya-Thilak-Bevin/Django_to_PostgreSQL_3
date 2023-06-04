from django.shortcuts import render
from .models import Company
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
       company=Company()
       code=request.POST.get('code')
       name=request.POST.get('name')
       date=request.POST.get('date')
       price=request.POST.get('price')
       volume=request.POST.get('volume')
       company.code=code
       company.name=name
       company.date=date
       company.price=price
       company.volume=volume
       company.save()
       return HttpResponse("<h1>Thanks For Contact Us</h1>")
    
    return render(request,'index.html')
