
from django.core import serializers
from django.http import HttpResponse

import json
from paypalcheckoutsdk.orders import OrdersGetRequest
from django.core import serializers
from django.http import HttpResponse

from .paypal import PayPalClient

from accounts.models import Address
from basket.basket import Basket
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from orders.models import Order, OrderItem

from .models import DeliveryOptions
# Create your views here.
@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "payment/delivery_choices.html", {"deliveryoptions": deliveryoptions})
@login_required
def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response
@login_required
def delivery_address(request):

    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
        

    addresses = Address.objects.filter(customer=request.user).filter("-default1")

    if "address" not in request.session:
        session["address"] = {"address_id": str(addresses[0].id)}
    else:
        session["address"]["address_id"] = str(addresses[0].id)
        session.modified = True
    address=Address.objects.filter(default=True)
    data = serializers.serialize("json",address)
    return render(request, "account/address.html", {"addresses": addresses,'data':data})


@login_required
def payment_complete(request):
    PPClient = PayPalClient()

    body = json.loads(request.body)
    data = body["orderID"]
    user_id = request.user.id
   

    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)

    total_paid = response.result.purchase_units[0].amount.value

    basket = Basket(request)
    address=Address.objects.filter(default=True).values()
   
    print(address[0]['full_name'])
    order = Order.objects.create(
        user_id=user_id,
        full_name=address[0]['full_name'],
        email=response.result.payer.email_address,
        address1=address[0]['address_line'],
        address2=address[0]['address_line2'],
        postal_code=address[0]['postcode'],
        country_code=address[0]['countrycode'],
        total_paid=response.result.purchase_units[0].amount.value,
        order_key=response.result.id,
        payment_option="paypal",
        billing_status=True,
    )
    order_id = order.pk

    for item in basket:
        OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

    return JsonResponse("Payment completed!", safe=False)


@login_required
def payment_successful(request):
    basket = Basket(request)
    basket.clear()
    address=Address.objects.filter(default=True)
    return render(request, "payment/payment_succesful.html", {"address":address})

def payment_selection(request):
    
   
    return render(request,'payment/payment_selection.html')

