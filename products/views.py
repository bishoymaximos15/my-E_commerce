from django.shortcuts import render
from . models import Product

# Create your views here.


def product_list(request):

        products=Product.objects.all()
        return render (request,'product_list.html',{'products':products})




def product_detail(request,id):
        detail=Product.objects.get(id=id)
        return render (request,'product_detail.html',{'item':detail})

