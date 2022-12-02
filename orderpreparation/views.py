from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View

from .models import *

# Create your views here.

def orderpreparation(request, customer_id):
    try:
        order_list = Orders.objects.all(customer_id = customer_id)
        milkshake_list = Milkshake.objects.all(order = txn_number)
        customizations_list = Customization.objects.all(tx_num = tx_number)
    except Orders.DoesNotExist:
        raise Http404("Order does not exist.")
    return render(request, 'orderpreparation.html', 
    {"order_list": order_list, "milkshake_list":milkshake_list, "customizations_list":customizations_list})


class HomePageView(View):
    def get(self, request):
        customer = Customer.objects.order_by("customer_name")
        return render(request, "orderpreparation/index.html", {"customer": customer})

