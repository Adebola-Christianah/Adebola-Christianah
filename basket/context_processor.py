import re
from .basket import Basket
from store.models import Product
def basket(request):
    return{'basket':Basket(request)}
def product(request):
    return{'product':Product.objects.all()}