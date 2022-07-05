from email.headerregistry import Address
from urllib import response


from .models import Address
from django.http import JsonResponse
def address(request):
    address=Address.objects.filter(default=True)
    return address
