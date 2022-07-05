

from decimal import Decimal
from django.shortcuts import get_object_or_404,  render
from .models import Category,Product
# Create your views here.
def home(request):
    products=Product.objects.filter(is_active=True)
    
    return render(request,'store/home.html',{'products':products})

def details(request,slug):
    product=get_object_or_404(Product,slug=slug,is_active=True)
    
    a=Decimal(product.discount_price)
    b=Decimal(product.regular_price)
    cutting=(a/b)*100
    percentage=cutting % 100
    percentage=int(100-percentage)
    context={'product':product,'discount':percentage}
    
    return render(request,'store/detail.html',context)
    
def category(request,category_slug): 
        categorize=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.filter(category=categorize)
       
        context={'product':product,'categorize':categorize}
        return render(request,'store/category.html',context)