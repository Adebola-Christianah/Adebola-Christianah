
from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .basket import Basket
from store.models import Product

# Create your views here.
def summary(request):
    return render(request,'basket/basket_home.html')
def addbasket(request):
    basket=Basket(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('productid'))
        qty=int(request.POST.get('product_qty'))
        products=get_object_or_404(Product,id=product_id)
        basket.add(product=products,qty=qty)
        basket_quantity=basket.__len__()
        response=JsonResponse({'quantity':basket_quantity})
        return response
def deletebasket(request):
    basket=Basket(request)
    if request.POST.get('action')=='post':
        product_id=request.POST.get('productid')
        basket.delete(product=product_id)
        basket_quantity=basket.__len__()
        baskettotal=basket.get_total_price()
        response=JsonResponse({'qty': basket_quantity, 'subtotal': baskettotal})
        return response
def updatebasket(request):
     basket=Basket(request)
     product_qty=int(request.POST.get('productqty'))
     product_id=int(request.POST.get('productid'))
     print(product_qty)
     print(product_id)
     basket.update(qty=product_qty,product=product_id)
     basket_quantity=basket.__len__()
     baskettotal=basket.get_total_price()
     print(basket_quantity)
     print(baskettotal)
     response=JsonResponse({'qty': basket_quantity, 'subtotal': baskettotal})
     return response
