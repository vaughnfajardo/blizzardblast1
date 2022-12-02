from django.shortcuts import render, redirect
from django.views import View

from .models import *

# Create your views here.


# QUERY
def refillingredient(request):
    refillingredient_list = Ingredient.objects.all().filter(quantity_on_hand__lte = 10)
    return render(request, "refillingredient.html", {'ingredient': refillingredient_list})

def orderslip(request, customer_id):
    customer_list = Customer.objects.get(customer_id=customer_id)
    order_list = Orders.objects.filter(customer_id=customer_list.customer_id)

    datadict = {
        "customer": customer_list,
        "order" : order_list,
    }
    
    return render(request, 'orderslip.html', datadict)

class HomePageView(View):
    def get(self, request):
        customer = Customer.objects.order_by("customer_name")
        return render(request, "index.html", {"customer": customer})




