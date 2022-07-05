
from django.http import JsonResponse
import json
from django.shortcuts import render,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import RegistrationForm,UserEditForm,UserAddressForm
from .token import accounts_activation_token
from .models import Customer
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .models import Address
from django.urls import reverse
from orders.models import Order


# Create your views here.
@login_required
def dashboard(request):
     
    return render(request,'accounts/user/dashboard.html')
@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'accounts/user/edit_details.html', {'user_form': user_form})
@login_required
def delete_user(request):
    user = Customer.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('accounts:delete_confirmation')
@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    address=Address.objects.filter(default=True)
    
    return render(request, "accounts/user/addresses.html", {"addresses": addresses})
@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("accounts:addresses"))
    else:
        address_form = UserAddressForm()
    return render(request, "accounts/user/edit_addresses.html", {"form": address_form})
@login_required
def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer=request.user)
        
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("accounts:addresses"))
    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address)
    return render(request, "accounts/user/edit_addresses.html", {"form": address_form})
@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    return redirect("accounts:addresses")

@login_required
def set_default(request, id):
    Address.objects.filter(customer=request.user, default=True).update(default=False)
    Address.objects.filter(pk=id, customer=request.user).update(default=True)
    return redirect("accounts:addresses")   
def default(request):
    address=Address.objects.filter(default=True)
    return JsonResponse(address,safe=False)
def register(request):
  #if request.user.is_authenticated:
     #   return redirect('/')
    if request.method == 'POST': 
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('accounts/registration/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': accounts_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
            registerForm = RegistrationForm()
    return render(request, 'accounts/registration/register.html', {'form': registerForm})
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(pk=uid)
    except: pass
    if user is not None and accounts_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('accounts:dashboard')
    else:
        return render(request, 'accounts/registration/invalid.html')
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return render(request,'accounts/user/user_orders.html',{'orders':orders})




