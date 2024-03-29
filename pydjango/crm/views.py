from django.shortcuts import render
from .models import Order
# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request,'./index.html',{'object_list':object_list})
def thanks_page(request):
    name = request.GET['name']
    phone = request.GET['phone']
    element = Order(order_name=name,order_phone=phone)
    element.save()
    return render(request,'./thanks_file.html',{'name':name,'phone':phone})